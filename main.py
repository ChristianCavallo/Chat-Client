import sys
import client
import json


SocketClient = client.SocketClient(('localhost', 15000))

SocketClient.sendMessage("ciao")


