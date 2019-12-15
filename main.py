from Connection import client
from events import Events
import json


def onConnect():
    print("Connected")

def onClosed():
    print("Connection closed")

def onMessageReceived(message):
    #Questa funzione viene chiamata ogni qual volta che arriva un messaggio dal server
    print("Received message: " + message)
    j = json.loads(message) #Carico il json
    id = j["id"] #Leggo l'id

    if id == -1: #Il command test ha id = -1
        print("Received a test: " + j["message"])

    if id == 21: # Una response di login
        print("Login response")

# Per trasmettere un messaggio bisogna creare un json con almeno l'id...
# Ogni messaggio ha il suo id (controlla la enum nella classe Command del c++). Una login request ha id = 20, mentre la sua
# corrispettiva response ha id = 21. Quindi trasmettiamo un messaggio id = 20 e ci aspettiamo un messaggio con 21
#                     loginJson = {"id": 20,
#                                  "email" : "test@test.it"
#                                  "password" : md5(password) o anche "12345" come prov
#                                 }
#                     loginJson = json.dumps(loginJson)
#                     SocketClient.sendMessage(loginJson)

events = Events()
SocketClient = client.SocketClient(('localhost', 15000))
SocketClient.events.onConnect += onConnect
SocketClient.events.onClosed += onClosed
SocketClient.events.onMessageReceived += onMessageReceived









