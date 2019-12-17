import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from ChatUi import Ui_Form
from Connection import client
from events import Events
import json


class Ui_ShowMedia(object):
    def setupUi(self, ShowMedia):
        ShowMedia.setObjectName("ShowMedia")
        ShowMedia.setMinimumSize(QtCore.QSize(800, 600))
        ShowMedia.setMaximumSize(QtCore.QSize(800, 600))

        self.scrollArea = QtWidgets.QScrollArea(ShowMedia)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.label)

        self.retranslateUi(ShowMedia)
        QtCore.QMetaObject.connectSlotsByName(ShowMedia)

    def retranslateUi(self, ShowMedia):
        _translate = QtCore.QCoreApplication.translate
        ShowMedia.setWindowTitle(_translate("ShowMedia", "Media Viewer"))

class MessageWidget(QtWidgets.QWidget):

    def __init__(self, media=None, parent=None):
        super(MessageWidget, self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setMinimumSize(QtCore.QSize(290, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(290, 350))

        self.subLayout = QtWidgets.QVBoxLayout()

        if not media == None:
            self.media = QtWidgets.QLabel()
            self.media.setMaximumHeight(200)
            self.media.setScaledContents(True)
            self.media.setStyleSheet("margin-top: 5px;")
            self.media.mousePressEvent = self.showMedia
            self.subLayout.addWidget(self.media)
            self.setMedia(media)

        self.textMessage = QtWidgets.QLabel()
        # self.textMessage.setGeometry(QtCore.QRect(10, 20, 271, 100))
        self.textMessage.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.textMessage.setWordWrap(True)
        self.textMessage.setStyleSheet("margin-top: 5px")
        self.subLayout.addWidget(self.textMessage)

        self.textTime = QtWidgets.QLabel()
        self.textTime.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        self.textTime.setText("--:--")
        font = QtGui.QFont()
        font.setItalic(True)
        self.textTime.setFont(font)

        self.subLayout.addWidget(self.textTime)

        self.groupBox.setLayout(self.subLayout)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textMessage.setFont(font)

        self.setLayout(self.layout)

    def setMessageStyle(self, received):
        if received:
            self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; margin-left: 5px;")
            self.layout.addWidget(self.groupBox)
            emptyText = QtWidgets.QLabel()
            self.layout.addWidget(emptyText)

        else:
            self.groupBox.setStyleSheet(
                "background-color:  rgb(219, 247, 197); border-radius: 10px; margin-right: 5px;")
            emptyText = QtWidgets.QLabel()
            self.layout.addWidget(emptyText)
            self.layout.addWidget(self.groupBox)

    def setMessageName(self, name):
        self.groupBox.setTitle(name + " said:")

    def setTime(self, time):
        self.textTime.setText(time)

    def setMedia(self, b):
        self.image = QtGui.QImage()
        bytearr = QtCore.QByteArray.fromBase64(bytes(b, "utf8"))
        self.image.loadFromData(bytearr, 'PNG')

        self.media.setPixmap(QtGui.QPixmap.fromImage(self.image))

    def showMedia(self, event):
        self.mediaForm = QtWidgets.QWidget()
        self.mediaUi = Ui_ShowMedia()
        self.mediaUi.setupUi(self.mediaForm)
        self.mediaUi.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.mediaForm.show()


def onConnect():
    print("Connected")


def onClosed():
    print("Connection closed")


def onMessageReceived(message):
    # Questa funzione viene chiamata ogni qual volta che arriva un messaggio dal server
    print("Received message: " + message)
    j = json.loads(message)  # Carico il json
    id = j["id"]  # Leggo l'id

    if id == -1:  # Il command test ha id = -1
        print("Received a test: " + j["message"])

    if id == 21:  # Una response di login
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
# SocketClient = client.SocketClient(('localhost', 15000))
# SocketClient.events.onConnect += onConnect
# SocketClient.events.onClosed += onClosed
# SocketClient.events.onMessageReceived += onMessageReceived

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

def clearMessages():
    ui.listWidget.clear()

def addMessage(message, showSender = True):
    myUser = "Christian"
    if message.get("media") is None:
        widget = MessageWidget()
    else:
        widget = MessageWidget(message.get("media"))

    widget.textMessage.setText(message["content"])  # Imposta il contenuto del messaggio
    widget.setTime(message["time"])  # Imposta il tempo del messaggio... potrebbe richiedere una formattazione del tipo hh:mm
    if showSender:
        widget.setMessageName(message["sender"])  # Nome di colui che invia... solo se è un gruppo.

    widget.setMessageStyle(myUser != message["sender"])  # True se ho ricevuto, False se l'ho inviato io

    # Create QListWidgetItem
    widgetItem = QtWidgets.QListWidgetItem(ui.listWidget)
    # Set size hint
    widgetItem.setSizeHint(widget.sizeHint())
    # Add QListWidgetItem into QListWidget
    ui.listWidget.addItem(widgetItem)
    ui.listWidget.setItemWidget(widgetItem, widget)
    ui.listWidget.scrollToBottom()


messages = [{"sender": "Christian",
             "time": "12:34",
             "content": "Ciao pollo come stai?"
             },

            {
                "sender" : "Pollo",
                "time" : "12:35",
                "content" : "Ciao chry, tutto bene tu?"
            },
            {
                "sender" : "Christian",
                "time" : "12:40",
                "content" : "Bene bene, tua madre è polla!"
            }]

for message in messages:
    addMessage(message, False)

sys.exit(app.exec_())
