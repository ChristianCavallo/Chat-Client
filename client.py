import socket
import struct
import sys
import json

from threading import Thread


class SocketClient(Thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stopFlag = False

    def __init__(self, address):
        self.address = address
        self.sock.connect(self.address)
        Thread.__init__(self)
        self.start()

    def run(self):
        try:

            print("Connected to the server")
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

                data = self.sock.recv(num)
                if len(data) != num:
                    print("Received " + len(data) + " but expected " + str(num))
                    continue

                message = data.decode("utf-8")

                data = self.sock.recv(4)
                num = struct.unpack('<i', data[:4])[0]
                if num != 43214321:
                    print("Wrong sync message. Waiting for a new one")
                    continue

                print("Received with success this message: " + message)
                if message != "ciao":
                    command = json.loads(message)
                    print("Getting the id: " + str(command["id"]))

        except:
            print("An exception occurred: " + sys.stderr)
            self.close()

        print("Closing the socket cause receive was 0.")
        self.close()

    def sendMessage(self, message):

        try:
            part1 = struct.pack("<I", 12344321)
            part2 = struct.pack("<I", len(message))
            part4 = struct.pack("<I", 43214321)
            self.sock.sendall(part1 + part2 + bytes(message, 'utf-8') + part4)

            print("Message sent to the server: " + message)



        except:
            print("An exception occurred: " + sys.stderr)
            self.close()

    def close(self):
        self.stopFlag = True
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        print("Socket closed.")
