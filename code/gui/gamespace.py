from PyQt5.QtGui import QPixmap
import gui
from gui import params
from gui.params import *


class GamespaceWindow(QWidget):

    def init_back_lbl(self):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(0, 0, gamespace_width, gamespace_height))
        label.setText("")
        label.setScaledContents(True)
        label.setObjectName("backlbl")
        return label

    def init_namelbl(self):
        namelbl = QtWidgets.QLabel(self.centralwidget)
        namelbl.setGeometry(QtCore.QRect(50, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        namelbl.setFont(font)
        namelbl.setStyleSheet("color:white;")
        namelbl.setObjectName("namelbl")
        return namelbl

    def init_avatarlbl(self):
        avatarlbl = QtWidgets.QLabel(self.centralwidget)
        avatarlbl.setGeometry(QtCore.QRect(30, 60, 180, 180))
        avatarlbl.setStyleSheet("background-color:white;\n"
                                "border-radius:90px;")
        avatarlbl.setObjectName("avatarlbl")
        pixmap = QPixmap(gui.player_global.get_avatar())
        avatarlbl.setPixmap(QPixmap(pixmap))
        avatarlbl.setScaledContents(True)

        return avatarlbl

    def init_levellbl(self):
        levellbl = QtWidgets.QLabel(self.centralwidget)
        levellbl.setGeometry(QtCore.QRect(260, 90, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        levellbl.setFont(font)
        levellbl.setStyleSheet("color:white;")
        levellbl.setObjectName("levellbl")
        return levellbl

    def init_levelprogress(self):
        levelprogress = QtWidgets.QProgressBar(self.centralwidget)
        levelprogress.setGeometry(QtCore.QRect(240, 150, 361, 41))
        levelprogress.setStyleSheet(level_progress_sheet)
        levelprogress.setProperty("value", gui.player_global.get_level_progress())
        levelprogress.setTextVisible(True)
        levelprogress.setObjectName("levelprogress")
        return levelprogress

    def init_gamelbl(self):
        gamelbl = QtWidgets.QLabel(self.centralwidget)
        gamelbl.setGeometry(QtCore.QRect(20, 310, 1821, 551))
        font = QtGui.QFont()
        font.setPointSize(23)
        gamelbl.setFont(font)
        gamelbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        gamelbl.setStyleSheet("background:rgba(85, 170, 255,0.3);")
        gamelbl.setObjectName("gamelbl")
        gamelbl.setText(" ")
        return gamelbl

    def init_profilebtn(self):
        profilebtn = QtWidgets.QPushButton(self.centralwidget)
        profilebtn.setGeometry(QtCore.QRect(760, 140, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        profilebtn.setFont(font)
        profilebtn.setStyleSheet("QPushButton{\n"
                                 "background-color:rgb(85, 170, 255);\n"
                                 "border-radius:15px;\n"
                                 "font-color:white;}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #6fbffc;\n"
                                 "}"
                                 )
        profilebtn.setObjectName("profilebtn")
        profilebtn.setText("Go To Profile")
        profilebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return profilebtn

    def init_connect4btn(self):
        connect4btn = QtWidgets.QPushButton(self.centralwidget)
        connect4btn.setGeometry(QtCore.QRect(50, 450, 400, 300))
        font = QtGui.QFont()
        font.setPointSize(13)
        connect4btn.setFont(font)
        connect4btn.setStyleSheet("QPushButton{\n"
                                 "background-color:#98BAE7;\n"
                                 "border-radius:5px;\n"
                                 "font-color:white;}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #F14A16;\n"
                                 "}" )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../storage/Icons/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        connect4btn.setIcon(icon1)
        connect4btn.setIconSize(QtCore.QSize(400, 250))
        connect4btn.setObjectName("connect4btn")
        connect4btn.setText(" ")
        connect4btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nameg = QtWidgets.QLabel(self.centralwidget)
        self.nameg.setGeometry(QtCore.QRect(175, 770, 145, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nameg.setFont(font)
        self.nameg.setStyleSheet("color:white;")
        self.nameg.setObjectName("namelbl")
        self.nameg.setText("Connect 4")
        return connect4btn

    def init_triviabtn(self):
        triviabtn = QtWidgets.QPushButton(self.centralwidget)
        triviabtn.setGeometry(QtCore.QRect(500, 450, 400, 300))
        font = QtGui.QFont()
        font.setPointSize(13)
        triviabtn.setFont(font)
        triviabtn.setStyleSheet("QPushButton{\n"
                                 "background-color:#98BAE7;\n"
                                 "border-radius:5px;\n"
                                 "font-color:white;}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #F14A16;\n"
                                 "}" )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../storage/Icons/trivia.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        triviabtn.setIcon(icon1)
        triviabtn.setIconSize(QtCore.QSize(300, 500))
        triviabtn.setObjectName("triviabtn")
        triviabtn.setText(" ")
        triviabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nameg = QtWidgets.QLabel(self.centralwidget)
        self.nameg.setGeometry(QtCore.QRect(650, 770, 145, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nameg.setFont(font)
        self.nameg.setStyleSheet("color:white;")
        self.nameg.setObjectName("namelbl")
        self.nameg.setText("Trivia")
        return triviabtn

    def init_exitbtn(self):
        exitbtn = QtWidgets.QPushButton(self.centralwidget)
        exitbtn.setGeometry(QtCore.QRect(50, 900, 80, 80))
        exitbtn.setText("")
        exitbtn.setStyleSheet(params.back_button_style)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../storage/Icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exitbtn.setIcon(icon)
        exitbtn.setIconSize(QtCore.QSize(50, 50))
        exitbtn.setAutoDefault(False)
        exitbtn.setFlat(False)
        exitbtn.setObjectName("exitbtn")
        exitbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return exitbtn

    def init_leaderboardbtn(self):
        leaderboardbtn = QtWidgets.QPushButton(self.centralwidget)
        leaderboardbtn.setGeometry(QtCore.QRect(1600, 130, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        leaderboardbtn.setFont(font)
        leaderboardbtn.setStyleSheet("QPushButton{\n"
                                     "background-color:rgba(245, 98, 3,0.9);\n"
                                     "border-radius:25px;\n"
                                     "color:white;}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #e87c35;\n"
                                     "}"
                                     "QPushButton:focus {\n"
                                     "     outline: none;box-shadow: none;\n"
                                     "}")
        leaderboardbtn.setObjectName("leaderboardbtn")
        leaderboardbtn.setText("leaderboard")
        leaderboardbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return leaderboardbtn

    def init_tournamentbtn(self):
        tournamentbtn = QtWidgets.QPushButton(self.centralwidget)
        tournamentbtn.setGeometry(QtCore.QRect(1400, 130, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        tournamentbtn.setFont(font)
        tournamentbtn.setStyleSheet("QPushButton{\n"
                                     "background-color:rgba(245, 98, 3,0.9);\n"
                                     "border-radius:25px;\n"
                                     "color:white;}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #e87c35;\n"
                                     "}")
        tournamentbtn.setObjectName("tournamentbtn")
        tournamentbtn.setText("tournament")
        tournamentbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return tournamentbtn

    def __init__(self, parent=None):
        super(GamespaceWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(gamespace_width, gamespace_height)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.back_lbl = self.init_back_lbl()
        self.avatarlbl = self.init_avatarlbl()
        self.namelbl = self.init_namelbl()
        self.levellbl = self.init_levellbl()
        self.levelprogress = self.init_levelprogress()
        self.profilebtn = self.init_profilebtn()
        self.exitbtn = self.init_exitbtn()
        self.leaderboardbtn = self.init_leaderboardbtn()
        self.tournamentbtn = self.init_tournamentbtn()
        self.gamelbl = self.init_gamelbl()
        self.connect4 = self.init_connect4btn()
        self.trivia = self.init_triviabtn()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", gamespace_title))


class GamespaceMain(QMainWindow):
    def __init__(self, parent=None):
        super(GamespaceMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(gamespace_width, gamespace_height)
        self.startUIWindow()
        self.movie = QMovie(gamespace_bcg)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = GamespaceWindow(self)
        self.setWindowTitle(gamespace_title)

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        self.Window.namelbl.setText(gui.player_global.get_name())
        self.Window.levellbl.setText("Level " + str(gui.player_global.get_level()))
        pixmap = QPixmap(gui.player_global.get_avatar())
        self.Window.avatarlbl.setPixmap(QPixmap(pixmap))
        self.Window.avatarlbl.setScaledContents(True)
        self.Window.levelprogress.setProperty("value", gui.player_global.get_level_progress())
        self.Window.levelprogress.setTextVisible(True)
        if type(gui.player_global).__name__ == 'Guest':
            self.Window.profilebtn.setVisible(False)
            self.Window.tournamentbtn.setVisible(False)
        else:
            self.Window.profilebtn.setVisible(True)
            self.Window.tournamentbtn.setVisible(True)
        print("refresh done")
