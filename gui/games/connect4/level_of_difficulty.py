from gui.params import *

class StartWindow(QWidget):

    def init_easy_btn(self):
        easy_btn = QtWidgets.QPushButton(self.layoutWidget)
        easy_btn.setFont(init_font_start(-1, True))
        easy_btn.setObjectName("easy_btn")
        easy_btn.setText("Easy")
        easy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return easy_btn

    def init_normal_btn(self):
        normal_btn = QtWidgets.QPushButton(self.layoutWidget)
        normal_btn.setFont(init_font_start(-1, True))
        normal_btn.setObjectName("normal_btn")
        normal_btn.setText("Normal")
        normal_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return normal_btn

    def init_hard_btn(self):
        hard_btn = QtWidgets.QPushButton(self.layoutWidget)
        hard_btn.setFont(init_font_start(-1, True))
        hard_btn.setObjectName("hard_btn")
        hard_btn.setText("Hard")
        hard_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return hard_btn

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
        window_title_lbl.setGeometry(QtCore.QRect(400, 170, 1200, 111))
        window_title_lbl.setFont(init_font_start(51, False))
        window_title_lbl.setStyleSheet("color:rgb(213, 221, 255);")
        window_title_lbl.setObjectName("window_title_lbl")
        window_title_lbl.setText("Select Your Difficulty")
        return window_title_lbl

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(gamespace_width, gamespace_height)
        self.setStyleSheet(startG_buttons_sheet)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 280, 421, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.easy_btn = self.init_easy_btn()
        self.verticalLayout.addWidget(self.easy_btn)
        self.normal_btn = self.init_normal_btn()
        self.verticalLayout.addWidget(self.normal_btn)
        self.hard_btn = self.init_hard_btn()
        self.verticalLayout.addWidget(self.hard_btn)
        self.quit_btn = self.init_quit_btn()
        self.quit_lbl = self.init_quitlbl()
        self.window_title_lbl = self.init_window_title()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "level of difficulty "))


class StartLevelMain(QMainWindow):
    def __init__(self, parent=None):
        super(StartLevelMain, self).__init__(parent)
        self.setGeometry(0, 0, 600, 750)
        self.setFixedSize(gamespace_width, gamespace_height)
        self.Window = StartWindow(self)
        self.movie = QMovie(startG_bcg)
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
        pass
        # gui.player_global = Player()
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StartLevelMain()
    w.show()
    sys.exit(app.exec_())
'''