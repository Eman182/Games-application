from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit

import gui
import params
from backend_layer.facade import Facade


class SignupWindow(QWidget):

    def __init__(self, parent=None):
        super(SignupWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(1383, 858)
        self.setFont(params.get_font(15))
        self.setStyleSheet("")
        # ####################################################################
        self.userNameLbl = self.get_username_label()
        self.signUpLbl = self.get_signup_label()
        self.passwordLbl = self.get_password_label()
        self.userNameTxtBox = self.get_username_txtbox()
        self.passwordTxtBox = self.get_password_txtbox()
        self.back_button = self.get_back_button()
        self.showPasswordBtn = self.get_show_password_button()
        self.genderLbl = self.get_gender_label()
        self.maleRdBtn = self.get_male_radiobutton()
        self.femaleRdBtn = self.get_female_radiobutton()
        self.invalidNameLbl = self.get_invalid_name_label()
        self.changePasswordLbl = self.get_change_password_label()
        self.checkGenderLbl = self.get_check_gender_label()
        self.next_button = self.get_next_button()

        self.userNameLbl.raise_()
        self.signUpLbl.raise_()
        self.passwordLbl.raise_()
        self.userNameTxtBox.raise_()
        self.passwordTxtBox.raise_()
        self.back_button.raise_()
        self.showPasswordBtn.raise_()
        self.genderLbl.raise_()
        self.maleRdBtn.raise_()
        self.femaleRdBtn.raise_()
        self.invalidNameLbl.raise_()
        self.changePasswordLbl.raise_()
        self.checkGenderLbl.raise_()
        self.next_button.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

    def get_username_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(240, 390, 291, 71))
        label.setFont(params.get_font(30))
        label.setStyleSheet("color: white;\n"
                            "background opacity: 0.0;")
        label.setScaledContents(False)
        label.setText("User Name")
        label.setObjectName("userNameLbl")
        return label

    def get_signup_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(80, 130, 381, 101))
        label.setFont(params.get_font(50))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Sign Up")
        label.setObjectName("signUpLbl")
        return label

    def get_password_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(250, 510, 271, 51))
        label.setFont(params.get_font(30))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Password")
        label.setObjectName("passwordLbl")
        return label

    def get_username_txtbox(self):
        txtbox = QtWidgets.QLineEdit(self)
        txtbox.setGeometry(QtCore.QRect(570, 390, 401, 51))
        txtbox.setFont(params.get_font(15))
        txtbox.setStyleSheet("background-color: rgba(230, 230, 230,0.6) ;\n"
                                          "border: 5px solid rgba(0,0,0,0) ;\n"
                                          "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                                          "color: #14279B ;\n"
                                          "padding-bottom:7px ;\n"
                                          "\n"
                                          "")
        txtbox.setPlaceholderText("Enter Your Name")
        txtbox.setText("")
        txtbox.setObjectName("userNameTxtBox")
        return txtbox

    def get_password_txtbox(self):
        txtbox = QtWidgets.QLineEdit(self)
        txtbox.setGeometry(QtCore.QRect(570, 500, 401, 51))
        txtbox.setFont(params.get_font(15))
        txtbox.setStyleSheet("background-color: rgba(230, 230, 230,0.6) ;\n"
                                          "border: 5px solid rgba(0,0,0,0) ;\n"
                                          "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                                          "color: #14279B ;\n"
                                          "padding-bottom:7px ;")
        txtbox.setEchoMode(QtWidgets.QLineEdit.Password)
        txtbox.setPlaceholderText("Enter Your Password")
        txtbox.setObjectName("passwordTxtBox")
        return txtbox

    def get_back_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(50, 770, 80, 80))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(params.back_button_style)
        button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../storage/Icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(50, 50))
        button.setAutoDefault(False)
        button.setFlat(False)
        button.setObjectName("pushButton")
        return button

    def get_show_password_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(920, 500, 51, 51))
        button.setStyleSheet(params.show_password_button_style)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../storage/Icons/showPassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon1)
        button.setIconSize(QtCore.QSize(80, 80))
        button.setText("")
        button.setObjectName("showPasswordBtn")
        button.clicked.connect(self.toggle_visibility)
        return button

    def get_gender_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(270, 630, 191, 81))
        label.setFont(params.get_font(30))
        label.setStyleSheet("color:white;")
        label.setText("Gender")
        label.setObjectName("genderLbl")
        return label

    def get_male_radiobutton(self):
        rdbtn = QtWidgets.QRadioButton(self)
        rdbtn.setGeometry(QtCore.QRect(560, 650, 151, 41))
        rdbtn.setFont(params.get_font(25))
        rdbtn.setStyleSheet("color:rgb(248, 255, 105);")
        rdbtn.setText("Male")
        rdbtn.setObjectName("maleRdBtn")
        return rdbtn
    
    def get_female_radiobutton(self):
        rdbtn = QtWidgets.QRadioButton(self)
        rdbtn.setGeometry(QtCore.QRect(810, 650, 221, 41))
        rdbtn.setFont(params.get_font(25))
        rdbtn.setStyleSheet("color:rgb(248, 255, 105);")
        rdbtn.setText("Female")
        rdbtn.setObjectName("femaleRdBtn")
        return rdbtn

    def get_invalid_name_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(990, 390, 221, 41))
        label.setFont(params.get_font(16))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setVisible(False)
        label.setText("Invalid Name")
        label.setObjectName("invalidNameLbl")
        return label
    
    def get_change_password_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(990, 510, 301, 31))
        label.setFont(params.get_font(18))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setVisible(False)
        label.setText("Invalid Password")
        label.setObjectName("changePasswordLbl")
        return label
    
    def get_check_gender_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(990, 510, 301, 330))
        label.setFont(params.get_font(18))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setText("Choose Gender!")
        label.setObjectName("checkGenderLbl")
        label.setVisible(False)
        return label
    
    def get_next_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(910, 800, 221, 51))
        button.setFont(params.get_font(20))
        button.setStyleSheet(params.next_button_style)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../storage/Icons/nextPage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon2)
        button.setText("Let\'s Go")
        button.setObjectName("next_pushButton")
        button.clicked.connect(self.get_user_password)
        return button

    def get_username(self):
        return self.userNameTxtBox.text()

    def get_user_password(self):
        return self.passwordTxtBox.text()

    def toggle_visibility(self):
        if self.passwordTxtBox.echoMode() == QLineEdit.Normal:
            self.passwordTxtBox.setEchoMode(QLineEdit.Password)
        else:
            self.passwordTxtBox.setEchoMode(QLineEdit.Normal)

    def get_gender(self):
        if self.maleRdBtn.isChecked():
            return False
        elif self.femaleRdBtn.isChecked():
            return True
        else:
            return None

    def sign_up_db(self):
        self.changePasswordLbl.setVisible(False)
        self.checkGenderLbl.setVisible(False)
        if self.get_gender() is None:
            self.checkGenderLbl.setVisible(True)
            return False

        elif len(self.get_user_password()) < 8:
            self.changePasswordLbl.setVisible(True)
            print("invalid")
            return False
        else:
            f = Facade.get_instance()
            print("facade created")
            check, player = f.signup_request(self.get_username(), self.get_user_password(), self.get_gender())
            print("check: ", check)
            print("player: ", player)
            if not check:
                self.invalidNameLbl.setVisible(True)
                return False
            else:
                gui.player_global = player
                return True



class SignupMain(QMainWindow):
    def __init__(self, parent=None):
        super(SignupMain, self).__init__(parent)
        self.setGeometry(0, 0, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/user.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = SignupWindow(self)
        self.setWindowTitle("My Program")

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        self.Window.userNameTxtBox.setText("")
        self.Window.passwordTxtBox.setText("")
        self.Window.femaleRdBtn.setChecked(False)
        self.Window.maleRdBtn.setChecked(False)

