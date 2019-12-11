import socket
import struct
import sys
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import rsa as rsa_

from threading import Thread


class Cryptographer(object):
    publickey = 0

    def __init__(self):
        (pubkey, privatekey) = rsa_.newkeys(1024)
        self.publickey = pubkey.save_pkcs1("PEM").decode("utf-8")
        self.key = RSA.import_key(privatekey.save_pkcs1("PEM").decode("utf-8"))
        self.decipher = PKCS1_OAEP.new(self.key)
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
        #print("Remaining: " + str(remainBytes))
        while remainBytes > 0:
            left = 80 * index
            right = left + 80

            if remainBytes < 80:
                right = left + len(message)
            #print("Left: " + str(left) + " Right: " + str(right))
            buffer += self.cipher_rsa.encrypt(message[left:right])
            index += 1
            remainBytes -= 80

        #print("Crypting keytimes " + str(keyTimes) + " Payload: " + str(len(buffer)) )
        return buffer

    def decrypt(self, message):
        keyTimes =  struct.unpack('<i', message[:4])[0]
        keySize = 128
        remainBytes = keySize * keyTimes
        buffer = bytearray()
        index = 0
        while remainBytes > 0:
            left = keySize * index + 4
            if remainBytes < keySize:
                right = left + remainBytes -1
            else:
                right = left + 128

            #print("Left: " + str(left) + " Right: " + str(right))
            part = self.decipher.decrypt(message[left:right])
            buffer += part
            index += 1
            remainBytes -= keySize
        return buffer

    def setServerKey(self, key):
        self.serverKey = RSA.import_key(key)
        self.cipher_rsa = PKCS1_OAEP.new(self.serverKey)



class SocketClient(Thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stopFlag = False
    isCrypted = False

    def __init__(self, address):
        self.address = address
        self.sock.connect(self.address)
        self.crypto = Cryptographer()
        Thread.__init__(self)
        self.start()

    def run(self):
        try:

            print("Connected to the server")
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

                if num < 0 or num > 1000000:
                    print("The length of payload isn't      ormal: " + str(num))
                    continue

                content = self.sock.recv(num)
                if len(content) != num:
                    print("Received " + len(content) + " but expected " + str(num))
                    continue



                data = self.sock.recv(4)
                num = struct.unpack('<i', data[:4])[0]
                if num != 43214321:
                    print("Wrong sync message. Waiting for a new one")
                    continue


                if not self.isCrypted:
                    message = content.decode("utf-8")
                    command = json.loads(message)
                    #print("Server sent his key: " + command["key"])
                    self.crypto.setServerKey(command["key"])
                    self.isCrypted = True
                    print("Connection crypted correctly")
                    testJson = {"id": 1,
                                 "test" : "ciao"
                                }
                    testJson = json.dumps(testJson)

                    self.sendMessage(testJson)
                else:
                    content = self.crypto.decrypt(content)
                    #print(content)
                    message = content.decode("utf-8")
                    print("Received with success this message: " + message)

        except ConnectionRefusedError:
            print("An exception occurred: " + str(sys.stderr))
            self.close()

        print("Closing the socket cause receive was 0.")
        self.close()

    def sendMessage(self, message):

        try:
            part1 = struct.pack("<I", 12344321)
            part2 = struct.pack("<I", len(message))
            content = bytes(message, 'utf-8')

            if self.isCrypted:
                content = self.crypto.encrypt(content)
                part2 = struct.pack("<I", len(content))

            part4 = struct.pack("<I", 43214321)

            self.sock.sendall(part1 + part2 + content + part4)

            print("Message sent to the server: " + message)

        except ConnectionRefusedError:
            print("An exception occurred: " + str(sys.stderr))
            self.close()

    def sendKey(self):
        keyJson = {"id": 0,
                   "key": self.crypto.publickey
                   }
        keyJson = json.dumps(keyJson)
        self.sendMessage(keyJson)

    def close(self):
        self.stopFlag = True
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        print("Socket closed.")
