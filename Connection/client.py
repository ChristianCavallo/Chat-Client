import socket
import struct
import sys
import json
import time
from threading import Thread

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
import rsa as rsa_
import base64
from Crypto.Util.Padding import pad

from PyQt5 import QtCore


class Cryptographer(object):


    def __init__(self):
        (pubkey, privatekey) = rsa_.newkeys(1024)
        self.publickey = pubkey.save_pkcs1("PEM").decode("utf-8")
        self.key = RSA.import_key(privatekey.save_pkcs1("PEM").decode("utf-8"))
        self.decipher = PKCS1_OAEP.new(self.key)
        print("Chiphers ready")

    def encrypt(self, message):
        # Impostare i primi 6 bytes di cui 5 -> Dimensione chiave

        keyTimes = int(len(message) / 80);
        remain = int(len(message) % 80);
        if keyTimes == 0:
            keyTimes += 1
        else:
            if remain > 0:
                keyTimes += 1

        buffer = bytearray()
        buffer += struct.pack("<I", keyTimes)

        remainBytes = len(message)
        index = 0
        # print("Remaining: " + str(remainBytes))
        while remainBytes > 0:
            left = 80 * index
            right = left + 80

            if remainBytes < 80:
                right = left + len(message)
            # print("Left: " + str(left) + " Right: " + str(right))
            buffer += self.cipher_rsa.encrypt(message[left:right])
            index += 1
            remainBytes -= 80

        # print("Crypting keytimes " + str(keyTimes) + " Payload: " + str(len(buffer)) )
        return buffer

    def decrypt(self, message):
        keyTimes = struct.unpack('<i', message[:4])[0]
        keySize = 128
        remainBytes = keySize * keyTimes
        buffer = bytearray()
        index = 0
        while remainBytes > 0:
            left = keySize * index + 4
            if remainBytes < keySize:
                right = left + remainBytes - 1
            else:
                right = left + 128

            # print("Left: " + str(left) + " Right: " + str(right))
            part = self.decipher.decrypt(message[left:right])
            buffer += part
            index += 1
            remainBytes -= keySize
        return buffer

    def setServerKey(self, key):
        self.serverKey = RSA.import_key(key)
        self.cipher_rsa = PKCS1_OAEP.new(self.serverKey)

    def setupAES(self, key, iv):
        self.aes_key = key
        self.aes_iv = iv

    def encrypt_AES(self, msg):

        self.cipher_aes = AES.new(self.aes_key, AES.MODE_CBC, self.aes_iv)
        buffer = bytearray()

        part = self.cipher_aes.encrypt(pad(msg, AES.block_size))
        buffer += struct.pack("<I", len(msg))
        buffer += part
        return buffer;

    def decrypt_AES(self, msg):
        self.cipher_aes = AES.new(self.aes_key, AES.MODE_CBC, self.aes_iv)
        len = struct.unpack('<i', msg[:4])[0]
        original = pad(self.cipher_aes.decrypt(msg[4:]), AES.block_size)[:len - 1]
        return original


class SocketClient(QtCore.QThread):
    onReceiveCallback = QtCore.pyqtSignal(object);
    onConnectCallback = None;
    onConnectionClosedCallback = None;

    def __init__(self, address):
        self.isCrypted_AES = False
        self.isCrypted_RSA = False
        self.stopFlag = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address

        self.crypto = Cryptographer()
        QtCore.QThread.__init__(self)
        self.start()

        self.keepAliveThread = Thread(target = self._keepAlive)
        self.receivedSomething = False

    def registerOnReceiveCallback(self, callback):
        self.onReceiveCallback = callback

    def registerOnConnectCallback(self, callback):
        self.onConnectCallback = callback

    def registerOnConnectionClosedCallback(self, callback):
        self.onConnectionClosedCallback = callback

    def reset(self):
        self.stopFlag = False
        self.isCrypted_AES = False
        self.isCrypted_RSA = False
        self.crypto = Cryptographer()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _keepAlive(self):
        while not self.stopFlag:
            time.sleep(30)
            if self.receivedSomething:
                self.receivedSomething = False
                continue

            msg = { "id" : 100 }
            msg = json.dumps(msg)
            self.sendMessage(msg)


    def run(self):
        while not self.stopFlag:
            try:
                print("Try to connect to the server")
                self.sock.connect(self.address)
            except:
                print("Can't reach the server.")
                #self.close()
                time.sleep(5)
                continue

            try:
                self.sendKey()

                while not self.stopFlag:
                    data = self.sock.recv(4)

                    if not len(data) > 0:
                        break

                    num = struct.unpack('<i', data[:4])[0]
                    if num != 12344321:
                        print("Wrong sync message. Received: " + str(num))
                        continue

                    data = self.sock.recv(4)
                    num = struct.unpack('<i', data[:4])[0]

                    if num < 0:
                        print("The length of payload isn't      ormal: " + str(num))
                        continue

                    content = bytearray()
                    while num > 0:
                        payload_part = self.sock.recv(num)

                        if len(payload_part) <= 0:
                            continue
                        num -= len(payload_part)
                        content += payload_part


                   # if len(content) != num:
                    #    print("Received " + len(content) + " but expected " + str(num))
                    #   continue

                    data = self.sock.recv(4)
                    num = struct.unpack('<i', data[:4])[0]
                    if num != 43214321:
                        print("Wrong sync message. Waiting for a new one")
                        continue

                    if not self.isCrypted_RSA and not self.isCrypted_AES:
                        content = self.crypto.decrypt(content)
                        message = content.decode("utf-8")
                        command = json.loads(message)
                        # print("Server sent his key: " + command["key"])
                        if not command["id"] == 0:
                            print("Invalid starting message from the server (Expected keys).")
                            self.close()
                            return

                        self.crypto.setServerKey(command["key-RSA"])
                        self.crypto.setupAES(base64.b64decode(command["key-AES"]), base64.b64decode(command["iv-AES"]))

                        self.isCrypted_RSA = True
                        self.isCrypted_AES = True

                        #self.events.onConnect()
                        self.onConnectCallback()
                        #testJson = {"id": -1,
                        #            "message": "ciao"
                        #            }
                        #testJson = json.dumps(testJson)

                        #self.sendMessage(testJson)

                    elif self.isCrypted_AES:
                        content = self.crypto.decrypt_AES(content)
                        message = content.decode("utf-8",)
                        j = json.loads(message)
                        self.receivedSomething = True
                        self.onReceiveCallback.emit(message)


            except:
                print("Socket error: " + str(sys.stderr))

            print("Connection lost.")
            self.close(True)

        print("Out scope, Thread is going to die.")

    def sendMessage(self, message):

        try:
            part1 = struct.pack("<I", 12344321)
            part2 = struct.pack("<I", len(message))
            content = bytes(message, 'utf-8')

            if self.isCrypted_AES:
                content = self.crypto.encrypt_AES(content)
                part2 = struct.pack("<I", len(content))

            part4 = struct.pack("<I", 43214321)


            self.sock.sendall(part1 + part2)

            if len(content) > 100*1024:
                print("I'm sending data larger than 100kb. I'm reporting the progress:")
                l = len(content)
                a = 0
                chunkSize = 100*1024
                progress = 0
                while(l > 0):
                    if l > chunkSize:
                        self.sock.sendall(content[a:(a+chunkSize)])
                        a += chunkSize
                        l -= chunkSize
                        progress = round(100 * a / (a+l), 2)
                        print("Sending percentage: " + str(progress) + "%")
                    else:
                        self.sock.sendall(content[a:(a+l)])
                        a += l
                        l = 0

                print("All sent.")
            else:
                self.sock.sendall(content)

            self.sock.sendall(part4)

        except:
            print("Exception on sending: " + str(sys.stderr))
            self.close(True)

    def sendKey(self):
        keyJson = {"id": 0,
                   "key": self.crypto.publickey
                   }
        keyJson = json.dumps(keyJson)
        self.sendMessage(keyJson)
        print("Sending my security keys...")

    def close(self, reset = False):
        self.stopFlag = True
        # self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.onConnectionClosedCallback()
        if reset:
            print("Resetting the connection.")
            self.reset()
        #self.events.onClosed()



