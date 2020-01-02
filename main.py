import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from ChatUi import Ui_Form
from Connection import client
from events import Events
import json
import base64
import hashlib

from Login import Ui_LoginForm
from Registration import Ui_Dialog_Registration
from Utils import Cacher



def showdialog(text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)

    msg.setText(text)
    msg.setWindowTitle("Chat Alert")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()

app = QtWidgets.QApplication(sys.argv)
LoginForm = QtWidgets.QMainWindow()
ui_Login = Ui_LoginForm()
ui_Login.setupUi(LoginForm)
LoginForm.show()

ChatForm = QtWidgets.QWidget()
ui_chat = Ui_Form()
ui_chat.setupUi(ChatForm)

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

    if id == 11: #Response di registrazione
        result= j["res"]
        print("Registration result: " + result)
        if result == "ok":
            ui_Login.Dialog_Registration.close()
        else:
            showdialog(result)

    if id == 21: # Una response di login
        #Qua riceviamo la risposta giusto?si, si chiama response
        print("Received message" + str(j))
        ui_chat.user_id = j["user-id"] #id poteva essere null oppure qualcosa.. giusto?

        if ui_chat.user_id is None:
            print("Wrong login!")
            showdialog("Wrong login!")

        else:
            ui_chat.name = j["name"]
            ui_chat.surname = j["surname"]
            
            ui_chat.userLabel.setText(ui_chat.name + " " + ui_chat.surname)
            print("Login success! " + ui_chat.user_id + "  " + ui_chat.name + " " + ui_chat.surname)
            LoginForm.close()



    if id == 31: # Add contact response
        result = j["result"]
        if result is True:
            pass
        else:
            pass

        pass

    if id == 41: # Una message response
        pass

    if id == 51: # Una create group response
        pass

    if id == 61:
        if j["media"] == "":
            print("Invalid media id")
            return

        for index in range(0, ui_chat.messagesList.count()):
            i = ui_chat.messagesList.itemWidget(ui_chat.messagesList.item(index))

            if i.media_id == j["media-id"]:
                i.setMedia(j["media"])
                Cacher.cacheMedia(j["media-id"], j["media"])
                break;

    if id == 71: # Una delete chat response
        result = j["result"]
        if result is True:
            fetchContacts()
        else:
            showdialog("Error while deleting the selected chat!")

    if id == 81: #Fetch contacts response
        initContactsView(j["chats"])

    if id == 91: #Fetch chat response
        initChatView(j)
    # TODO: Se la chat che sto fetchando non è un gruppo, mi aspetto che nella risposta ci sia anche l'ultimo accesso dell'interlocutore.


events = Events()
SocketClient = client.SocketClient(('localhost', 15000))
SocketClient.events.onConnect += onConnect
SocketClient.events.onClosed += onClosed
SocketClient.events.onMessageReceived += onMessageReceived


#=============== LOGIN SIGNALS ======================

def login():
    password = ui_Login.lineEdit_password.text().strip()
    message = {"id": 20,
               "email": ui_Login.lineEdit_email.text().strip(),
               "password": hashlib.md5(password.encode()).hexdigest()
               }
    print("Sending a login request with data: " +  str(message))
    message = json.dumps(message)
    SocketClient.sendMessage(message)

def openWindowRegistration():
    LoginForm.hide()

    ui_Login.Dialog_Registration = QtWidgets.QDialog()
    ui_Login.ui_registration = Ui_Dialog_Registration()
    ui_Login.ui_registration.setupUi(ui_Login.Dialog_Registration)

    ui_Login.ui_registration.Signup_toolButton.clicked.connect(register)

    ui_Login.Dialog_Registration.exec_()
    LoginForm.show()

def register():
    password = ui_Login.ui_registration.lineEdit_password.text().strip()

    req = { "id" : 10,
            "name" : ui_Login.ui_registration.lineEdit_name.text().strip(),
            "surname" :  ui_Login.ui_registration.lineEdit_surname.text().strip(),
            "email" :  ui_Login.ui_registration.lineEdit_email.text().strip(),
            "password" :  hashlib.md5(password.encode()).hexdigest()
            }

    req = json.dumps(req)
    SocketClient.sendMessage(req)

ui_Login.pushButton_Login.clicked.connect(login)
ui_Login.pushButton_createAccount.clicked.connect(openWindowRegistration)

#====================================================

code = app.exec_()
print("Login form closed with code " + str(code))


#app = QtWidgets.QApplication(sys.argv)

ChatForm.show()

# ==================== WIDGETS =================================
class ChatWidget(QtWidgets.QWidget):

    def __init__(self, isGroup=False, parent=None):
        super(ChatWidget, self).__init__(parent)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.toolButton = QtWidgets.QToolButton()
        self.toolButton.setMaximumSize(QtCore.QSize(50, 50))
        icon = QtGui.QIcon()
        if isGroup:
            icon.addPixmap(QtGui.QPixmap("Resources/group_contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(QtGui.QPixmap("Resources/user_contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.label = QtWidgets.QLabel()
        self.label.setMaximumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setText("Christian Cavallo")
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.notificationLabel = QtWidgets.QLabel()
        self.notificationLabel.setMaximumSize(QtCore.QSize(21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.notificationLabel.setFont(font)
        self.notificationLabel.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 10px;")
        self.notificationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notificationLabel.setText("2")

        self.horizontalLayout.addWidget(self.toolButton)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.notificationLabel)

        self.setLayout(self.horizontalLayout)

    def addNotifies(self, text):
        self.notificationLabel.setText(text)

    def cleanNotifies(self):
        self.notificationLabel.setText("0")
        self.notificationLabel.hide()


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

    def __init__(self, media_id=None, parent=None):
        super(MessageWidget, self).__init__(parent)

        self.media_id = media_id

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setMinimumSize(QtCore.QSize(290, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(290, 350))

        self.subLayout = QtWidgets.QVBoxLayout()
        self.subLayout.setSpacing(0)
        if not media_id == None:
            data = Cacher.getCachedMedia(media_id)
            self.media = QtWidgets.QLabel()
            self.downloadMediaToolButton = QtWidgets.QToolButton()
            self.media.setMaximumHeight(200)
            self.media.setMinimumHeight(200)
            self.media.setScaledContents(True)
            self.media.setStyleSheet("margin-top: 5px;")
            self.media.mousePressEvent = self.showMedia
            self.subLayout.addWidget(self.media)
            if data is not None:

                self.setMedia(data)
            else:
                self.media.hide()
                self.downloadMediaToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                self.downloadMediaToolButton.setMaximumHeight(200)
                self.downloadMediaToolButton.setMinimumHeight(200)

                self.downloadMediaToolButton.setMinimumWidth(280)
                icon1 = QtGui.QIcon()

                icon1.addPixmap(QtGui.QPixmap("Resources/download_media.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.downloadMediaToolButton.setIcon(icon1)

                self.downloadMediaToolButton.setIconSize(QtCore.QSize(100, 100))
                self.downloadMediaToolButton.clicked.connect(self.getMedia)
                self.subLayout.addWidget(self.downloadMediaToolButton)

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

    def getMedia(self):
        data = Cacher.getCachedMedia(self.media_id)
        if not data is None:
            self.setMedia(data)

        else:

            icon = QtGui.QIcon()

            icon.addPixmap(QtGui.QPixmap("Resources/loading.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.downloadMediaToolButton.setIcon(icon)
            self.downloadMediaToolButton.clicked.disconnect()

            m = {"id": 60,
                 "media-id": self.media_id
                 }
            m = json.dumps(m)
            SocketClient.sendMessage(m)

    def setTime(self, time):
        self.textTime.setText(time)

    def setMedia(self, b):
        self.downloadMediaToolButton.hide()
        self.media.show()

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


# ===============================================================


# ========================CHATUI SIGNALS=====================================

def clearMessages():
    ui_chat.messagesList.clear()


def addMessage(message, showSender=True):

    myUser = ui_chat.user_id
    if message.get("media") is None:
        widget = MessageWidget()
    else:
        widget = MessageWidget(message.get("media"))

    widget.textMessage.setText(message["content"])  # Imposta il contenuto del messaggio
    widget.setTime(
        message["time"])  # TODO: Imposta il tempo del messaggio... potrebbe richiedere una formattazione del tipo hh:mm
    if showSender:
        widget.setMessageName(message["sender"])  # Nome di colui che invia... solo se è un gruppo.

    widget.setMessageStyle(myUser != message["sender"])  # True se ho ricevuto, False se l'ho inviato io

    # Create QListWidgetItem
    widgetItem = QtWidgets.QListWidgetItem(ui_chat.messagesList)
    # Set size hint
    widgetItem.setSizeHint(widget.sizeHint())
    # Add QListWidgetItem into QListWidget
    ui_chat.messagesList.addItem(widgetItem)
    ui_chat.messagesList.setItemWidget(widgetItem, widget)
    ui_chat.messagesList.scrollToBottom()


def clearContacts():
    ui_chat.chatList.clear()


def addContact(chat):
    contact = ChatWidget(chat.get("isGroup"))
    contact.label.setText(chat.get("name"))

    if not chat.get("notifies") is None:
        contact.addNotifies(chat.get("notifies"))

    widgetItem = QtWidgets.QListWidgetItem(ui_chat.chatList)
    contact.id = chat.get("chat-id")
    contact.user_id = chat.get("contact-id")
    contact.isGroup = chat.get("isGroup")

    widgetItem.setSizeHint(contact.sizeHint())
    ui_chat.chatList.addItem(widgetItem)
    ui_chat.chatList.setItemWidget(widgetItem, contact)




def sendMessage(self):
    text = ui_chat.messageText.text().strip()

    m = {
        "id": "40",
        "chat-id": ui_chat.selectedChat.id,
        "text": text,
        "media": ui_chat.media
    }

    m = json.dumps(m)

    # TODO: SEND THIS MESSAGE TO THE SERVER AND COMPLETE THE RECEPTION OF NEW MESSAGES AS WELL
    SocketClient.sendMessage(m)
    #print(m)

    if ui_chat.media is not None:
        removeMediaToolButton_clicked()


def showFileDialog():
    dlg = QtWidgets.QFileDialog()
    dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
    dlg.setNameFilter("Images (*.png *.gif *.jpg)")

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        size = os.path.getsize(filenames[0])
        if size > 5 * 1024 * 1024:
            showdialog("The file is too large to be sent.")
            return

        f = open(filenames[0], 'rb')

        with f:
            data = f.read()
            m = base64.b64encode(data)
            ui_chat.media = str(m, "utf-8")

            print("Media selected: " + str(size) + " bytes")
            ui_chat.removeMediaToolButton.setEnabled(True)


def removeMediaToolButton_clicked():
    ui_chat.removeMediaToolButton.setEnabled(False)
    ui_chat.media = None
    print("Media cleaned!")




def addGroupToolButton_Clicked():
    ui_chat.groupNameText.show()
    ui_chat.groupNameText.setText("")
    ui_chat.addGroupToolButton.setEnabled(False)
    ui_chat.confirmGroupToolButton.show()
    ui_chat.cancelGroupToolButton.show()
    ui_chat.chatList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
    ui_chat.isSelectingGroup = True


def confirmGroupToolButton_Clicked():
    if len(ui_chat.chatList.selectedItems()) > 1:

        items = ui_chat.chatList.selectedItems()

        ids = []
        for item in items:
            i = ui_chat.chatList.itemWidget(item)
            if i.isGroup:
                showdialog("You can't add a group in a group!")
                item.setSelected(False)
                return
            ids.append(i.id)

        name = ui_chat.groupNameText.text().strip()

        if name == "":
            name = "My new group"

        j = {"id": 50,
             "ids": ids,
             "name" : name
             }

        j = json.dumps(j)

        SocketClient.sendMessage(j)

        cancelGroupButton_clicked()

    else:
        print("Select at least 2 contacts.")
        showdialog("Select at least 2 contacts.")


def cancelGroupButton_clicked():
    ui_chat.confirmGroupToolButton.hide()
    ui_chat.cancelGroupToolButton.hide()
    ui_chat.groupNameText.hide()
    ui_chat.addGroupToolButton.setEnabled(True)
    ui_chat.chatList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    ui_chat.chatList.clearSelection()
    ui_chat.isSelectingGroup = False


def logoutButton_clicked():
    ChatForm.close()
    SocketClient.close()


def chatList_CurrentItemChanged(new, previous):
    if not ui_chat.isSelectingGroup:
        fetchSelectedChat()

def addContactButton_clicked():
    email = ui_chat.searchContactLabel.text().strip()
    from email.utils import parseaddr
    email = parseaddr(email)

    if len(email) < 3 or not email.cont:
        showdialog("Insert a valid email address please.")
        return

    req = {
        "id": "30",
        "email": email
    }

    req = json.dumps(req)
    SocketClient.sendMessage(req)
    # TODO: SEND THE REQUEST TO THE SERVER TO ADD A NEW CONTACT


def removeChatButton_clicked():
    if ui_chat.selectedChat is not None:
        r = {
            "id": "70",
            "chat-id": ui_chat.selectedChat.id,
            "isGroup": ui_chat.selectedChat.isGroup
        }

        r = json.dumps(r)
        SocketClient.sendMessage(r)


#=========================CHAT VIEW======================================
def resetChatView():
    clearMessages()
    ui_chat.headerChatFrame.hide()
    ui_chat.sendBarFrame.setEnabled(False)

def initChatView(j):
    chatName = j["name"]
    ui_chat.labelChatName.setText(chatName)

    status = j["status"]

    icon = QtGui.QIcon()
    if status == "online":
        icon.addPixmap(QtGui.QPixmap("Resources/green_dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    else:
        icon.addPixmap(QtGui.QPixmap("Resources/red_dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    ui_chat.statusToolButton.setIcon(icon)
    ui_chat.statusToolButton.show()

    ui_chat.labelStatus.setText(status)

    ui_chat.headerChatFrame.show()
    ui_chat.sendBarFrame.show()

    ui_chat.messageText.setText("")
    removeMediaToolButton_clicked()

    isGroup = j["isgroup"]

    if isGroup:
        ui_chat.statusToolButton.hide()

    #TODO: LOAD MESSAGES... j["messages"] e addMessage
    for message in j["messages"]:

        addMessage(message, isGroup)


def initContactsView(j):
    ui_chat.loadedContacts.clear()
    ui_chat.chatList.clear()

    for chat in j:
        addContact(chat)
        ui_chat.loadedContacts.append(chat)



ui_chat.chatList.currentItemChanged.connect(chatList_CurrentItemChanged)
ui_chat.selectedChat = None

ui_chat.confirmGroupToolButton.hide()
ui_chat.cancelGroupToolButton.hide()

ui_chat.addGroupToolButton.clicked.connect(addGroupToolButton_Clicked)
ui_chat.confirmGroupToolButton.clicked.connect(confirmGroupToolButton_Clicked)
ui_chat.cancelGroupToolButton.clicked.connect(cancelGroupButton_clicked)
ui_chat.isSelectingGroup = False

ui_chat.removeMediaToolButton.clicked.connect(removeChatButton_clicked)

ui_chat.mediaToolButton.clicked.connect(showFileDialog)
ui_chat.removeMediaToolButton.clicked.connect(removeMediaToolButton_clicked)
ui_chat.media = None

ui_chat.sendToolButton.clicked.connect(sendMessage)

ui_chat.addContactToolButton.clicked.connect(addContactButton_clicked)

ui_chat.logoutToolButton.clicked.connect(logoutButton_clicked)

ui_chat.groupNameText.hide()

ui_chat.loadedContacts = []

# ===========================================================================

def fetchContacts():
    r = {
        "id": 80
    }

    r = json.dumps(r)
    SocketClient.sendMessage(r)


def removeSelectedChat():
    if ui_chat.selectedChat is not None:
        r = {
            "id": 70,
            "chat-id": ui_chat.selectedChat.id,
            "isGroup": ui_chat.selectedChat.isGroup
        }

        r = json.dumps(r)
        SocketClient.sendMessage(r)


def fetchSelectedChat():
    con = ui_chat.chatList.itemWidget(ui_chat.chatList.item(ui_chat.chatList.currentRow()))
    ui_chat.selectedChat = con
    m = {"id": 90,
         "chat-id": ui_chat.selectedChat.id
         }
    m = json.dumps(m)
    SocketClient.sendMessage(m)
    print("Fetching chat: " + str(ui_chat.selectedChat.id))




messages = [{"sender": "Christian",
             "time": "12:34",
             "content": "Ciao pollo come stai?"
             },
            {
                "sender": "Pollo",
                "time": "12:35",
                "content": "Ciao chry, tutto bene tu?"
            },
            {
                "sender": "Christian",
                "time": "12:40",
                "content": "Bene bene, tua madre è polla!",
                "media": "CgiKs1vudDn0HTPoUhN5Z7IOqBaE2lbM"
            }]

for message in messages:
    addMessage(message, False)

contacts = [
    {"chat-id": "abcd123abcd",
     "contact-id" : "132dhuid",
     "name": "Christian Cavallo",
     "isGroup": False},
    {"contact-id": "abc123789bcdasf",
     "name": "Ciao Pollo",
     "isGroup": False},
    {"contact-id": "ab8679cd",
     "name": "Kirito Harem",
     "isGroup": True},
    {"contact-id": "a234432233abcd",
     "name": "Babbo Natale",
     "isGroup": False}
]


for contact in contacts:
    #addContact(contact)
    ui_chat.loadedContacts.append(contact)


fetchContacts()

code = app.exec_()
SocketClient.close()
sys.exit(code)
# sys.exit(app.exec_())
