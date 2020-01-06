import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from ChatUi import Ui_Chat
from Connection import client
import json
import base64
import hashlib

from Login import Ui_LoginForm
from Registration import Ui_Dialog_Registration
from Utils import Cacher


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

LoginForm = QtWidgets.QMainWindow()
ui_Login = Ui_LoginForm()
ui_Login.setupUi(LoginForm)
LoginForm.show()


ChatForm = QtWidgets.QWidget()
ui_chat = Ui_Chat()
ui_chat.setupUi(ChatForm)
ui_chat.user_id  = None


def showdialog(text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)

    msg.setText(text)
    msg.setWindowTitle("Chat Alert")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    app.processEvents()
    msg.exec_()

    print("Done")



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



    if id == 31 or id == 51 or id == 71 : # Add contact response - delete chat response - create group response
        result = j["result"]
        if result is True:
            fetchContacts()
        else:
            showdialog(j["content"])

    if id == 41: # Una message response
        chatid = j["chat-id"]
        #primo caso la chat selezionata ha lo stesso id
        if ui_chat.selectedChat is not None:
            if ui_chat.selectedChat.id == chatid:
                addMessage(j, ui_chat.selectedChat.isGroup)
                return

        #secondo caso: la chat è nella lista ma non è selezionata
        for index in range(0, ui_chat.chatList.count()):
            i = ui_chat.chatList.itemWidget(ui_chat.chatList.item(index))

            if i.id == chatid:
                i.addNotify()
                return;

        #terzo caso: la chat non è nella lista
        fetchContacts()


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

    if id == 81: #Fetch contacts response
        initContactsView(j["chats"])

    if id == 91: #Fetch chat response
        initChatView(j)
    # TODO: Se la chat che sto fetchando non è un gruppo, mi aspetto che nella risposta ci sia anche l'ultimo accesso dell'interlocutore.


SocketClient = client.SocketClient(('localhost', 15000))

#SocketClient.registerOnReceiveCallback(onMessageReceived)
SocketClient.onReceiveCallback.connect(onMessageReceived)
SocketClient.registerOnConnectCallback(onConnect)
SocketClient.registerOnConnectionClosedCallback(onClosed)




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

if ui_chat.user_id is None:
    SocketClient.close()
    sys.exit(0)

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
        self.notificationLabel.setText("0")

        self.horizontalLayout.addWidget(self.toolButton)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.notificationLabel)

        self.setLayout(self.horizontalLayout)

    def setNotifies(self, n):
        self.notificationLabel.setText(str(n))
        if n == 0:
            self.notificationLabel.hide()
        else:
            self.notificationLabel.show()


    def clearNotifies(self):
        self.setNotifies(0)

    def addNotify(self):
        self.notificationLabel.show()
        a = int(self.notificationLabel.text())
        a += 1
        self.notificationLabel.setText(str(a))

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

    def __init__(self, media_id=None, showSender=False, parent=None):
        super(MessageWidget, self).__init__(parent)

        self.media_id = media_id

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

        self.frameBox = QtWidgets.QFrame()
        self.frameBox.setMinimumSize(QtCore.QSize(290, 50))
        self.frameBox.setMaximumSize(QtCore.QSize(290, 350))

        self.subLayout = QtWidgets.QVBoxLayout()
        self.subLayout.setSpacing(0)

        self.nameLabel = QtWidgets.QLabel()
        self.nameLabel.setStyleSheet("color: rgb(178, 0, 0);")
        font1 = QtGui.QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.nameLabel.setFont(font1)
        if showSender:
            self.subLayout.addWidget(self.nameLabel)

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
        #self.textMessage.setStyleSheet("margin-top: 5px")
        self.subLayout.addWidget(self.textMessage)

        self.textTime = QtWidgets.QLabel()
        self.textTime.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        self.textTime.setText("--:--")
        font = QtGui.QFont()
        font.setItalic(True)
        self.textTime.setFont(font)

        self.subLayout.addWidget(self.textTime)


        self.frameBox.setLayout(self.subLayout)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textMessage.setFont(font)

        self.setLayout(self.layout)

    def setMessageStyle(self, received):
        if received:
            self.frameBox.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; margin-left: 5px;")
            self.layout.addWidget(self.frameBox)
            emptyText = QtWidgets.QLabel()
            self.layout.addWidget(emptyText)

        else:
            self.frameBox.setStyleSheet(
                "background-color:  rgb(219, 247, 197); border-radius: 10px; margin-right: 5px;")
            emptyText = QtWidgets.QLabel()
            self.layout.addWidget(emptyText)
            self.layout.addWidget(self.frameBox)

    def setMessageName(self, name):
        self.nameLabel.setText(name)

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
    if message.get("media") == "":
        widget = MessageWidget(None, (showSender and myUser != message["sender_id"]))
    else:
        widget = MessageWidget(message.get("media"), (showSender and myUser != message["sender_id"]))

    widget.textMessage.setText(message["content"])  # Imposta il contenuto del messaggio
    widget.setTime(
        message["time"])
    if showSender:
        widget.setMessageName(message["senderName"])  # Nome di colui che invia... solo se è un gruppo.

    widget.setMessageStyle(myUser != message["sender_id"])  # True se ho ricevuto, False se l'ho inviato io

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

    contact.setNotifies(chat.get("notifies"))

    widgetItem = QtWidgets.QListWidgetItem(ui_chat.chatList)
    contact.id = chat.get("chat-id")
    contact.user_id = chat.get("contact-id")
    contact.isGroup = chat.get("isGroup")

    widgetItem.setSizeHint(contact.sizeHint())
    ui_chat.chatList.addItem(widgetItem)
    ui_chat.chatList.setItemWidget(widgetItem, contact)




def sendMessage(self):
    text = ui_chat.messageText.text().strip()
    media = ui_chat.media
    if media is None:
        media = ""
    m = {
        "id": 40,
        "chat-id": ui_chat.selectedChat.id,
        "content": text,
        "media": media
    }

    m = json.dumps(m)

    SocketClient.sendMessage(m)
    #print(m)
    ui_chat.messageText.clear()
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

            print("Media selected: " + str(size) + " bytes: " + ui_chat.media)

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
            ids.append(i.user_id)

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


def chatList_CurrentItemChanged(new, previous):
    if not ui_chat.isSelectingGroup:
        if new is not None :
            con = ui_chat.chatList.itemWidget(ui_chat.chatList.item(ui_chat.chatList.currentRow()))
            ui_chat.selectedChat = con
            fetchSelectedChat()
        else:
            clearChatView()

def addContactButton_clicked():
    email = ui_chat.searchContactLabel.text().strip()
    print("email: " + email)
    from email.utils import parseaddr
    email = parseaddr(email)[1]
    print("email dopo: " + email)
    if len(email) < 3:
        showdialog("Insert a valid email address please.")
        return

    req = {
        "id": 30,
        "email": email
    }
    ui_chat.searchContactLabel.clear()
    req = json.dumps(req)
    SocketClient.sendMessage(req)


def removeChatButton_clicked():
    removeSelectedChat()


#=========================CHAT VIEW======================================

def clearChatView():
    clearMessages()
    ui_chat.headerChatFrame.hide()
    ui_chat.sendBarFrame.setEnabled(False)

def initChatView(j):
    chatName = ui_chat.selectedChat.label.text()
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
    ui_chat.sendBarFrame.setEnabled(True)

    ui_chat.messageText.setText("")
    removeMediaToolButton_clicked()

    isGroup = ui_chat.selectedChat.isGroup

    if isGroup:
        ui_chat.statusToolButton.hide()

    clearMessages()
    for message in j["messages"]:

        addMessage(message, isGroup)

    ui_chat.selectedChat.clearNotifies()


def initContactsView(j):
    ui_chat.loadedContacts.clear()
    ui_chat.chatList.clear()

    for chat in j:
        addContact(chat)
        ui_chat.loadedContacts.append(chat)


#ui_chat.messageText.installEventFilter()

ui_chat.chatList.currentItemChanged.connect(chatList_CurrentItemChanged)
ui_chat.selectedChat = None

ui_chat.confirmGroupToolButton.hide()
ui_chat.cancelGroupToolButton.hide()

ui_chat.addGroupToolButton.clicked.connect(addGroupToolButton_Clicked)
ui_chat.confirmGroupToolButton.clicked.connect(confirmGroupToolButton_Clicked)
ui_chat.cancelGroupToolButton.clicked.connect(cancelGroupButton_clicked)
ui_chat.isSelectingGroup = False


ui_chat.mediaToolButton.clicked.connect(showFileDialog)
ui_chat.removeMediaToolButton.clicked.connect(removeMediaToolButton_clicked)
ui_chat.media = None

ui_chat.sendToolButton.clicked.connect(sendMessage)

ui_chat.addContactToolButton.clicked.connect(addContactButton_clicked)

ui_chat.logoutToolButton.clicked.connect(logoutButton_clicked)

ui_chat.groupNameText.hide()

ui_chat.loadedContacts = []
ui_chat.selectedChat = None

ui_chat.removeChatToolButton.clicked.connect(removeChatButton_clicked)

clearChatView()

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
            "chat-id": ui_chat.selectedChat.id
        }

        r = json.dumps(r)
        SocketClient.sendMessage(r)


def fetchSelectedChat():
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
                "id-sender" : "aisjfsjafso",
                "sender": "Christian",
                "time": "12:40",
                "content": "Bene bene, tua madre è polla!",
                "media": "CgiKs1vudDn0HTPoUhN5Z7IOqBaE2lbM"
            }]

#for message in messages:
    #addMessage(message, False)

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
