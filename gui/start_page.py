from params import *
import gui
from backend_layer.models.guest import Guest

class StartWindow(QWidget):
    def init_signin_btn(self):
        signin_btn = QtWidgets.QPushButton(self.layoutWidget)
        signin_btn.setFont(init_font_start(-1, True))
        signin_btn.setObjectName("signin_btn")
        signin_btn.setText("Sign In")
        signin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return signin_btn

    def init_signup_btn(self):
        signup_btn = QtWidgets.QPushButton(self.layoutWidget)
        signup_btn.setFont(init_font_start(-1, True))
        signup_btn.setObjectName("signup_btn")
        signup_btn.setText("Sign Up")
        signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return signup_btn

    def init_guest_btn(self):
        guest_btn = QtWidgets.QPushButton(self.layoutWidget)
        guest_btn.setFont(init_font_start(-1, True))
        guest_btn.setObjectName("guest_btn")
        guest_btn.setText("Play as a guest")
        guest_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        gui.player_global = Guest()
        return guest_btn

    def init_quit_btn(self):
        quit_btn = QtWidgets.QPushButton(self)
        quit_btn.setGeometry(QtCore.QRect(50, 890, 81, 81))
        quit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        quit_btn.setStyleSheet("QPushButton{\n"
                                 "background-color:rgba(152,186,231,0.7);\n"
                                 "border-radius: 40px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color:#98BAE7;\n"
                                 "}\n"
                                 "")
        quit_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../storage/Icons/sign-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        quit_btn.setIcon(icon1)
        quit_btn.setIconSize(QtCore.QSize(80, 80))
        quit_btn.setObjectName("quit_btn")
        return quit_btn

    def init_quitlbl(self):
        quitlbl = QtWidgets.QLabel(self)
        quitlbl.setGeometry(QtCore.QRect(55, 830, 81, 81))
        quitlbl.setFont(init_font_start(15, False))
        quitlbl.setStyleSheet("color:rgb(213, 221, 255);")
        quitlbl.setObjectName("quitlbl")
        quitlbl.setText("Quit")
        return quitlbl
    def init_window_title(self):
        window_title_lbl = QtWidgets.QLabel(self)
        window_title_lbl.setGeometry(QtCore.QRect(650, 170, 591, 111))
        window_title_lbl.setFont(init_font_start(51, False))
        window_title_lbl.setStyleSheet("color:rgb(213, 221, 255);")
        window_title_lbl.setObjectName("window_title_lbl")
        window_title_lbl.setText("BLACK HoLE")
        return window_title_lbl

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(gamespace_width, gamespace_height)
        self.setStyleSheet(startpg_buttons_sheet)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 280, 421, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signin_btn = self.init_signin_btn()
        self.verticalLayout.addWidget(self.signin_btn)
        self.signup_btn = self.init_signup_btn()
        self.verticalLayout.addWidget(self.signup_btn)
        self.guest_btn = self.init_guest_btn()
        self.quit_btn = self.init_quit_btn()
        self.quit_lbl = self.init_quitlbl()
        self.verticalLayout.addWidget(self.guest_btn)
        self.window_title_lbl = self.init_window_title()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BLACK HoLE"))


class StartMain(QMainWindow):
    def __init__(self, parent=None):
        super(StartMain, self).__init__(parent)
        self.setGeometry(0, 0, 600, 750)
        self.setFixedSize(gamespace_width, gamespace_height)
        self.Window = StartWindow(self)
        self.setWindowTitle(startpage_title)
        self.movie = QMovie(start_bcg)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        gui.player_global = Guest()
