from backend_layer.facade import Facade
from gui.params import *


class TournamentSetupWindow(QWidget):
    def init_starttour_btn(self):
        pc_btn = QtWidgets.QPushButton(self)
        pc_btn.setFont(init_font_start(-1, True))
        pc_btn.setGeometry(QtCore.QRect(1700, 890, 150, 81))
        pc_btn.setObjectName("start_tour")
        pc_btn.setText("Start")
        pc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return pc_btn

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
        window_title_lbl.setGeometry(QtCore.QRect(550, 90, 900, 111))
        window_title_lbl.setFont(init_font_start(51, False))
        window_title_lbl.setStyleSheet("color:rgb(213, 221, 255);")
        window_title_lbl.setObjectName("window_title_lbl")
        window_title_lbl.setText("Setup tournament")
        return window_title_lbl

    def get_game_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(370, 330, 351, 81))
        label.setFont(get_font(25))
        label.setStyleSheet("color:white;")
        label.setText("Select Game")
        label.setObjectName("gameLbl")
        return label

    def get_connect4_radiobutton(self):
        rdbtn = QtWidgets.QRadioButton(self)
        rdbtn.setGeometry(QtCore.QRect(720, 355, 251, 41))
        rdbtn.setFont(get_font(25))
        rdbtn.setStyleSheet("color:rgb(248, 255, 105);")
        rdbtn.setText("Connect 4")
        rdbtn.setObjectName("connect4RdBtn")
        return rdbtn

    def get_trivia_radiobutton(self):
        rdbtn = QtWidgets.QRadioButton(self)
        rdbtn.setGeometry(QtCore.QRect(1050, 355, 221, 41))
        rdbtn.setFont(get_font(25))
        rdbtn.setStyleSheet("color:rgb(248, 255, 105);")
        rdbtn.setText("Trivia")
        rdbtn.setObjectName("triviaRdBtn")
        return rdbtn

    def check_rdBtn(self, radio_button):
        # Uncheck every other button in this group
        for button in self.rdBtnGroup.buttons():
            if button is not radio_button:
                button.setChecked(False)

    def get_check_game_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(1290, 210, 301, 330))
        label.setFont(get_font(18))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setText("Choose Game!")
        label.setObjectName("checkGameLbl")
        label.setVisible(False)
        return label

    def get_playername_label(self, pname, offx, offy):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(200 + offx, 520 + offy, 291, 71))
        label.setFont(get_font(20))
        label.setStyleSheet("color: white;\n"
                            "background opacity: 0.0;")
        label.setScaledContents(False)
        label.setText(pname + " Name")
        label.setObjectName(pname + "Lbl")
        return label

    def get_playername_txtbox(self, pname, offx, offy):
        txtbox = QtWidgets.QLineEdit(self)
        txtbox.setGeometry(QtCore.QRect(480 + offx, 530 + offy, 350, 51))
        txtbox.setFont(get_font(15))
        txtbox.setStyleSheet("background-color: rgba(230, 230, 230,0.6) ;\n"
                             "border: 5px solid rgba(0,0,0,0) ;\n"
                             "bordar-bottom-color:rgba(46,82,101,200) ;\n"
                             "color: #14279B ;\n"
                             "padding-bottom:7px ;\n"
                             "\n"
                             "")
        txtbox.setPlaceholderText("Enter " + pname + " Name")
        txtbox.setText("")
        txtbox.setObjectName(pname + "TxtBox")
        return txtbox

    def get_checknames_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(200, 430, 500, 41))
        label.setFont(get_font(20))
        label.setStyleSheet("color:rgb(255,69,72);\n")
        label.setVisible(False)
        label.setText("Enter All Players Names !")
        label.setObjectName("checknamesLbl")
        return label

    def get_game(self):
        if self.connect4RdBtn.isChecked():
            return 'connect4'
        elif self.triviaRdBtn.isChecked():
            return 'trivia'
        else:
            return None

    def start_tournament(self):
        self.checknamesLbl.setVisible(False)
        self.checkGameLbl.setVisible(False)
        if self.get_game() is None:
            self.checkGameLbl.setVisible(True)
            return False

        if len(self.p1TxtBox.text()) == 0 or len(self.p2TxtBox.text()) == 0 \
                or len(self.p3TxtBox.text()) == 0 or len(self.p4TxtBox.text()) == 0:
            self.checknamesLbl.setVisible(True)
            return False

        f = Facade.get_instance()
        game = self.get_game()
        print("game :", game)
        players = [self.p1TxtBox.text(), self.p2TxtBox.text(), self.p3TxtBox.text(), self.p4TxtBox.text()]
        print("players :", players)
        return f.create_tournament(game, players)

    def __init__(self, parent=None):
        super(TournamentSetupWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(gamespace_width, gamespace_height)
        self.setStyleSheet(startG_buttons_sheet)
        self.start_tour_btn = self.init_starttour_btn()
        self.quit_btn = self.init_quit_btn()
        self.quit_lbl = self.init_quitlbl()
        self.gameLbl = self.get_game_label()
        self.connect4RdBtn = self.get_connect4_radiobutton()
        self.triviaRdBtn = self.get_trivia_radiobutton()
        # Radio buttons
        self.rdBtnGroup = QtWidgets.QButtonGroup()
        self.rdBtnGroup.setExclusive(False)  # Radio buttons are not exclusive
        self.rdBtnGroup.addButton(self.connect4RdBtn)
        self.rdBtnGroup.addButton(self.triviaRdBtn)
        self.rdBtnGroup.buttonClicked.connect(self.check_rdBtn)

        self.checkGameLbl = self.get_check_game_label()
        # players names
        self.p1Lbl = self.get_playername_label("Player1", 0, 0)
        self.p1TxtBox = self.get_playername_txtbox("Player1", 0, 0)

        self.p2Lbl = self.get_playername_label("Player2", 800, 0)
        self.p2TxtBox = self.get_playername_txtbox("Player2", 800, 0)

        self.p3Lbl = self.get_playername_label("Player3", 0, 200)
        self.p3TxtBox = self.get_playername_txtbox("Player3", 0, 200)

        self.p4Lbl = self.get_playername_label("Player4", 800, 200)
        self.p4TxtBox = self.get_playername_txtbox("Player4", 800, 200)

        self.checknamesLbl = self.get_checknames_label()
        self.window_title_lbl = self.init_window_title()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setup tournament"))


class TournamentSetupMain(QMainWindow):
    def __init__(self, parent=None):
        super(TournamentSetupMain, self).__init__(parent)
        self.setGeometry(0, 0, 600, 750)
        self.setFixedSize(gamespace_width, gamespace_height)
        self.Window = TournamentSetupWindow(self)
        self.setWindowTitle("Setup tournament")
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
        self.Window.checknamesLbl.setVisible(False)
        self.Window.checkGameLbl.setVisible(False)
        self.Window.p1TxtBox.setText("")
        self.Window.p2TxtBox.setText("")
        self.Window.p3TxtBox.setText("")
        self.Window.p4TxtBox.setText("")
        self.Window.connect4RdBtn.setChecked(False)
        self.Window.triviaRdBtn.setChecked(False)


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TournamentSetupMain()
    w.show()
    sys.exit(app.exec_())
'''