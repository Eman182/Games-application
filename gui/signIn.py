from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit

import gui
import params
from backend_layer.facade import Facade


class SigninWindow(QWidget):

    def __init__(self, parent=None):
        super(SigninWindow, self).__init__(parent)
        # self.setObjectName("Form")
        self.resize(1938, 1043)
        self.setFont(params.get_font(15))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("D:/CSED/Third Year/First Semester/SE/project/space/space/icons/icons8-space-64.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # self.setWindowIcon(params.app_icon)
        self.setWindowTitle("Sign In")
        # ###################################################################################################3

        self.background = self.get_background()
        self.title_label = self.get_title_label()
        self.username_label = self.get_username_label()
        self.password_label = self.get_password_label()
        self.username_lineEdit = self.get_username_lineEdit()
        self.password_lineEdit = self.get_password_lineEdit()
        self.show_password_button = self.get_show_password_button()
        self.invalid_username_label = self.get_invalid_username_label()
        self.invalid_password_label = self.get_invalid_password_label()
        self.back_button = self.get_back_button()
        self.next_button = self.get_next_button()

        self.background.raise_()
        self.title_label.raise_()
        self.username_label.raise_()
        self.password_label.raise_()
        self.username_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.show_password_button.raise_()
        self.invalid_username_label.raise_()
        self.invalid_password_label.raise_()
        self.back_button.raise_()
        self.next_button.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

    def get_title_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(80, 130, 361, 91))
        label.setFont(params.get_font(50))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Sign In")
        label.setObjectName("title_label")
        return label

    def get_username_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(240, 390, 281, 61))
        label.setFont(params.get_font(30))
        label.setStyleSheet("color: white;\n"
                            "background opacity: 0.0;")
        label.setScaledContents(False)
        label.setText("User Name")
        label.setObjectName("username_label")
        return label

    def get_password_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(250, 510, 251, 61))
        label.setFont(params.get_font(30))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Password")
        label.setObjectName("password_label")
        return label

    def get_username_lineEdit(self):
        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(570, 400, 401, 51))
        lineEdit.setFont(params.get_font(15))
        lineEdit.setStyleSheet(params.sign_in_lineEdit_style)
        lineEdit.setPlaceholderText("Enter Your Name")
        lineEdit.setText("")
        lineEdit.setObjectName("username_lineEdit")
        return lineEdit

    def get_password_lineEdit(self):
        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(570, 510, 401, 51))
        lineEdit.setFont(params.get_font(15))
        lineEdit.setStatusTip("")
        lineEdit.setStyleSheet(params.sign_in_lineEdit_style)
        lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        lineEdit.setPlaceholderText("Enter Your Password")
        lineEdit.setObjectName("password_lineEdit")
        return lineEdit

    def get_background(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, -10, 2621, 1081))
        label.setFont(params.get_font(10))
        label.setStyleSheet(params.background_style)
        label.setText("")
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setScaledContents(True)
        label.setObjectName("background")
        return label

    def get_back_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(50, 900, 81, 81))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(params.back_button_style)
        button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../storage/Icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(80, 80))
        button.setObjectName("back_pushButton")
        return button

    def get_show_password_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(910, 510, 61, 51))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(params.show_password_button_style)
        button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../storage/Icons/showPassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon2)
        button.setIconSize(QtCore.QSize(50, 50))
        button.setObjectName("show_password_pushButton")
        button.clicked.connect(self.toggle_visibility)
        return button

    def get_next_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(910, 650, 221, 51))
        button.setFont(params.get_font(20))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(params.next_button_style)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../storage/Icons/nextPage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon3)
        button.setIconSize(QtCore.QSize(100, 100))
        button.setText("Let\'s GO")
        button.setObjectName("next_pushButton")
        return button

    def get_invalid_username_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(990, 400, 401, 51))
        label.setFont(params.get_font(18))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setVisible(False)
        label.setText("User doesn't exist")
        label.setObjectName("invalidNameLbl")
        return label

    def get_invalid_password_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(990, 510, 401, 51))
        label.setFont(params.get_font(18))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setVisible(False)
        label.setText("Incorrect password")
        label.setObjectName("changePasswordLbl")
        return label

    def get_username(self):
        return self.username_lineEdit.text()

    def get_user_password(self):
        return self.password_lineEdit.text()

    def toggle_visibility(self):
        print(gui.player_global)
        if self.password_lineEdit.echoMode() == QLineEdit.Normal:
            self.password_lineEdit.setEchoMode(QLineEdit.Password)
        else:
            self.password_lineEdit.setEchoMode(QLineEdit.Normal)

    def sign_in_db(self):
        self.invalid_username_label.setVisible(False)
        self.invalid_password_label.setVisible(False)
        f = Facade.get_instance()
        # check > boolean, response > player object
        check, response = f.signin_request(self.get_username(), self.get_user_password())
        if not check:  # response is an error msg
            print(response)
            if response == "Player doesn't exist!":
                self.invalid_username_label.setVisible(True)
            elif response == "Wrong password!":
                self.invalid_password_label.setVisible(True)
            return False
        else:
            gui.player_global = response
            return True


class SigninMain(QMainWindow):
    def __init__(self, parent=None):
        super(SigninMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/user.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = SigninWindow(self)
        self.setWindowTitle("My Program")

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        self.Window.username_lineEdit.setText("")
        self.Window.password_lineEdit.setText("")
