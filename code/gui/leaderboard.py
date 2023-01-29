from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QGraphicsDropShadowEffect

import params
from backend_layer.facade import Facade


class LeaderboardWindow(QWidget):

    def __init__(self, parent=None):
        super(LeaderboardWindow, self).__init__(parent)
        # self.setObjectName("Form")
        self.resize(1938, 1043)
        self.setFont(params.get_font(15))

        # self.setWindowIcon(params.app_icon)
        self.setWindowTitle("Leaderboard")
        # ###################################################################################################

        self.tableWidget = self.get_table()
        #self.read_list([("player 2", "20"),("player 2", "20"),("player 2", "20"),("player 2", "20"),])
        '''self.read_list([("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40"),
                        ("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40"),
                        ("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40"),
                        ("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40"),
                        ("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40"),
                        ("player 1", "10"),
                        ("player 2", "20"),
                        ("player 3", "30"),
                        ("player 4", "40")])'''

        self.background = self.get_background()
        self.title_label = self.get_title_label()
        self.frame = self.get_frame()
        self.back_button = self.get_back_button()

        self.background.raise_()
        self.title_label.raise_()

        self.back_button.raise_()
        self.tableWidget.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

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

    def get_title_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(660, 40, 631, 81))
        label.setFont(params.get_font(50))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Leader Board")
        label.setObjectName("title_label")
        return label

    def get_frame(self):
        frame = QtWidgets.QFrame(self)
        frame.setGeometry(QtCore.QRect(570, 200, 800, 700))
        frame.setStyleSheet(params.leaderboard_frame_style)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        color = QtGui.QColor(229, 206, 235, 100)
        shadow.setColor(color)
        frame.setGraphicsEffect(shadow)
        frame.setObjectName("frame")
        return frame

    def get_table(self):
        tableWidget = QtWidgets.QTableWidget(self)
        tableWidget.setColumnCount(2)
        tableWidget.setGeometry(QtCore.QRect(570, 200, 800, 700))
        tableWidget.setHorizontalHeaderLabels(('Player', 'XP'))
        tableWidget.verticalScrollBar().setStyleSheet(params.scroll_style)
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        tableWidget.setStyleSheet(params.background_style)
        tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        tableWidget.horizontalHeader().setFixedHeight(70)
        tableWidget.resizeRowsToContents()
        tableWidget.setShowGrid(False)
        tableWidget.setFocus(False)
        tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        tableWidget.horizontalHeader().setDisabled(True)
        tableWidget.horizontalHeader().setFocus(False)
        tableWidget.setCornerButtonEnabled(False)
        #tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        tableWidget.setStyleSheet(params.leaderboard_tabel_style)
        return tableWidget

    def read_list(self, items):
        # item : list of players records (tuple)
        print(items)
        self.tableWidget.setRowCount(len(items))
        for i, item in enumerate(items):
            cell1 = QtWidgets.QTableWidgetItem(item[0])
            cell2 = QtWidgets.QTableWidgetItem("        " + str(item[1]) + "        ")
            cell1.setTextAlignment(QtCore.Qt.AlignCenter)
            cell2.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, cell1)
            self.tableWidget.setItem(i, 1, cell2)


class LeaderboardMain(QMainWindow):
    def __init__(self, parent=None):
        super(LeaderboardMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/user.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = LeaderboardWindow(self)
        self.setWindowTitle("My Program")

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        f = Facade.get_instance()
        leaderboard_list = f.get_leaderboard()
        self.Window.read_list(leaderboard_list)
