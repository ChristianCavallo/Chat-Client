from PyQt5 import QtWidgets

from Connection import client
from events import Events
import json

from Login import Ui_MainWindow
from Registration import Ui_Dialog_Registration


def onRegistration(message):
    #i dati ora arrivano qua
    print(message)


def onConnect():
    print("Connected")
    #Questa funzione viene chiamata non appena siamo connessi
    #per prima cosa devi definire i "COMANDI".
    # La facciamo qua, lo scopo di questo comando è ottenere un email e password...
    #nomeJson = {"id": 20,
    #            "email": lg[0], #dove prende lg? è nella casse login che cià i valori che vengono presi quando scriviamo email e password
    #            "password":lg[1]
    #            }
    # trasformiamolo in stringa json
    #nomeJson = json.dumps(nomeJson)  # Questo crea la stringa { id : 22, val : "", val1: "" }
    #SocketClient.sendMessage(nomeJson)  # visto?
    # fatto, adesso stiamo mandando una richiesta con id 22 e val = 2, andiamo nel server per gestire la richiesta ok?ok

    # Resta l'ultima cosa da fare.... noi mandiamo una richiesta 22... il server ci ritorna una 23... e dove la leggo? giusto?si dove la legge? xD

    # Emm si... dobbiamo aspettare di essere connessi, prima di mandare un messaggio giustamente...

    #Cambiamo il valore di val a 1... cosi dovrebbe mandare "Christian" giusto?sisi
    #è bellissimo xD cosa xD mi piace sto sistema xD tutto protetto in AES viaggia xD
    #Sapresti rifarlo adesso?penso di si xD io ti avevo gia creato gli id delle richieste login e registrazione

def onClosed():
    print("Connection closed")

def onMessageReceived(message):
    #dentro questa funzione xD, il "message" sarà quella stringa che manda il server
    #Questa funzione viene chiamata ogni qual volta che arriva un messaggio dal server
    print("Received message: " + message) #ci aspettiamo che arrivi { "id" : 23, "name" : "Noemi", "altroValore" : 12345}
    #giusto?
    j = json.loads(message) #Carico il json
    id = j["id"] #Leggo l'id

    if id == -1: #Il command test ha id = -1
        print("Received a test: " + j["message"])

    if id == 21: # Una response di login
        #Qua riceviamo la risposta giusto?si, si chiama response
        print("Received message" + str(j))
        id = j["user-id"] #lo avevamo chiamato cosi l'id giusto?sisi.. poteva essere null oppure qualcosa.. giusto?

        #semplice no? no....per me sembra visto semplice fatto da te xD
        if id is None:
            print("Wrong login!")

        else:
            name = j["name"]
            surname = j["surname"]

            print("Login success! " + id + "  " + name + " " + surname)



    if id == 23:
        name = j["name"];
        valore = j["altroValore"]
        print("Ciao sono " + name + "  e altroValore è " + str(valore)) #str trasforma qualsiasi cosa in stringa... visto che altrovalore è un numero


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

import sys
#app = QtWidgets.QApplication(sys.argv)
#Dialog_Registration = QtWidgets.QDialog()
#ui = Ui_Dialog_Registration()
#ui.setupUi(Dialog_Registration)
#Dialog_Registration.show()
#ui.events.onRegistrationDone += onRegistration #ma al con tempo ci registriamo come ascoltatori per la funzione onRegistrationDone
#sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show() #cmq è un problema sta cosa... xke io avvio la dashboard direttamente, mentre tu avvii il login...
#devo pensare a come far coesistere ste cose


#=============== LOGIN SIGNALS ======================

def login():
    message = {"id": 20,
               "email": ui.lineEdit_email.text(),
               "password": ui.lineEdit_password.text()
               }
    print("Sending a login request with data: " +  str(message))
    message = json.dumps(message)
    SocketClient.sendMessage(message)

ui.pushButton_Login.clicked.connect(login)

#La cosa buona di collegare tutto in questo modo, è che puoi modificare il file Login.py tutte le volte che vuoi e nn devi
#fare copia e incolla ogni volta che fai "python -m ...."

#====================================================

sys.exit(app.exec_())









