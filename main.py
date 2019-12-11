from Connection import client
import rsa
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import struct




SocketClient = client.SocketClient(('localhost', 15000))



