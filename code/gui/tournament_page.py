import sys

from PyQt5 import QtCore, QtWidgets, QtTest
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QGraphicsDropShadowEffect, QApplication, QAbstractItemView

import params
from backend_layer.facade import Facade


class TournamentWindow(QWidget):

    def __init__(self, parent=None):
        super(TournamentWindow, self).__init__(parent)
        # self.setObjectName("Form")
        self.resize(1938, 1043)
        self.move(-5, -5)
        self.setFont(params.get_font(15))

        # self.setWindowIcon(params.app_icon)
        self.setWindowTitle("Tournament")
        # ###################################################################################################

        self.tableWidget = self.get_table()
        # self.read_list([("player 2", "20"),("player 2", "20"),("player 2", "20"),("player 2", "20"),])
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

        '''g = Guest.build_guest("test tour")
        lis = [{"player": g, "color": "blue", "wins": 0}, {"player": g, "color": "yellow", "wins": 0},
               {"player": g, "color": "green", "wins": 0}, {"player": g, "color": "black", "wins": 0},
               {"player": g, "color": "green", "wins": 0}, {"player": g, "color": "black", "wins": 0}]
        self.read_list(lis)'''

        self.background = self.get_background()
        self.title_label = self.get_title_label()
        self.next_match_label = self.get_next_match_label()
        self.p1_label = self.get_player_label(200, 'green', 'Player 1')
        self.p2_label = self.get_player_label(555, 'red', 'Player 2')
        self.x_label = self.get_x_label()
        self.winner_label = self.get_winner_label()
        self.frame = self.get_frame()
        self.back_button = self.get_back_button()
        self.start_button = self.get_start_button()

        self.background.raise_()
        self.title_label.raise_()

        self.back_button.raise_()
        self.start_button.raise_()
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

    def get_start_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(400, 700, 250, 80))
        button.setStyleSheet(params.startG_buttons_sheet)
        button.setText("Start")
        button.setObjectName("start_pushButton")
        return button

    def get_title_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(660, 40, 631, 81))
        label.setFont(params.get_font(50))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Tournament")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("title_label")
        return label

    def get_next_match_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(160, 350, 800, 81))
        label.setFont(params.get_font(40))
        label.setStyleSheet("color: white")
        label.setScaledContents(False)
        label.setText("Next to go :")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("next_match_label")
        return label

    def get_player_label(self, x_dim, color, player):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(x_dim, 510, 300, 80))
        label.setFont(params.get_font(25))
        label.setStyleSheet("color: {};{}".format(color, params.tournament_player_label_style))
        label.setScaledContents(False)
        label.setText("Player")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName(player + "_label")
        return label

    def get_x_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(375, 525, 300, 50))
        label.setFont(params.get_font(35))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("X")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("x_label")
        return label

    def get_winner_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(240, 490, 700, 50))
        label.setFont(params.get_font(35))
        label.setStyleSheet("color: white;")
        label.setScaledContents(False)
        label.setText("Winner")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("winner_label")
        return label

    def get_frame(self):
        frame = QtWidgets.QFrame(self)
        frame.setGeometry(QtCore.QRect(1100, 230, 480, 550))
        frame.setStyleSheet(params.tournament_frame_style)
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
        tableWidget.setGeometry(QtCore.QRect(1100, 230, 480, 550))
        tableWidget.setHorizontalHeaderLabels(['Player', '# wins'])
        tableWidget.verticalScrollBar().setStyleSheet(params.scroll_style)
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # tableWidget.setStyleSheet(params.background_style)
        tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        tableWidget.horizontalHeader().setFixedHeight(60)
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        tableWidget.setSortingEnabled(False)
        tableWidget.resizeRowsToContents()
        tableWidget.setShowGrid(False)
        tableWidget.setFocus(False)
        tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        tableWidget.horizontalHeader().setDisabled(True)
        tableWidget.horizontalHeader().setFocus(False)
        tableWidget.setCornerButtonEnabled(False)
        tableWidget.setDisabled(False)
        # tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        tableWidget.setStyleSheet(params.tournament_tabel_style)
        return tableWidget

    def read_list(self, items):
        # item : list of tournament players (dictionary)
        if items is None:
            return
        items = sorted(items, key=lambda d: (d['state'], d['wins']), reverse=True)
        print(items)
        self.tableWidget.setRowCount(len(items))
        for i, item in enumerate(items):
            cell1 = QtWidgets.QTableWidgetItem(item['player'].get_name())
            cell2 = QtWidgets.QTableWidgetItem(str(item['wins']))
            cell1.setTextAlignment(QtCore.Qt.AlignCenter)
            cell2.setTextAlignment(QtCore.Qt.AlignCenter)

            if item['state']:
                brush = QtGui.QBrush(QtGui.QColor(item['color']))
                brush.setStyle(QtCore.Qt.SolidPattern)
            else:
                brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
                brush.setStyle(QtCore.Qt.SolidPattern)

            cell1.setForeground(brush)
            # cell1.setBackground(QtGui.QColor('red'))
            cell2.setForeground(brush)
            # cell2.setBackground(brush2)

            self.tableWidget.setItem(i, 0, cell1)
            self.tableWidget.setItem(i, 1, cell2)
            self.tableWidget.setRowHeight(i, 100)
            # self.tableWidget.item(i, 1).setBackground(item['color'])

    def set_players(self, match):
        if match is not None:
            p1, p2 = match
            print(p1['player'].get_name(), p2['player'].get_name())
            print(p1['color'], p2['color'])
            self.p1_label.setText(p1['player'].get_name())
            self.p2_label.setText(p2['player'].get_name())
            self.p1_label.setStyleSheet("color: {}; {}".format(p1['color'], params.tournament_player_label_style))
            self.p2_label.setStyleSheet("color: {}; {}".format(p2['color'], params.tournament_player_label_style))


class TournamentMain(QMainWindow):
    def __init__(self, parent=None):
        super(TournamentMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.move(0, 0)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/gamespace.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = TournamentWindow(self)
        self.setWindowTitle("My Program")

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        print("inside tournament_page refresh")
        f = Facade.get_instance()
        match = f.get_next_match()
        players_list = f.get_tournament_players()
        # print("got a match in tournament_page, ", match[])
        self.Window.read_list(players_list)
        self.Window.set_players(match)
        if match is None:
            print('Tournament is over!')
            winner = f.get_winner()
            self.Window.winner_label.setText(f"Winner:{winner['player'].get_name()}")
            self.Window.winner_label.setVisible(True)
            self.Window.p1_label.setVisible(False)
            self.Window.p2_label.setVisible(False)
            self.Window.x_label.setVisible(False)
            self.Window.start_button.setVisible(False)
            self.Window.next_match_label.setText("Tournament is over!")

            color = ["rgb(255, 3, 112)", winner['color']]
            for i in range(20):
                self.Window.winner_label.setStyleSheet(f"color: {color[i % 2]};")
                #self.upd()
                #self.repaint()
                QtTest.QTest.qWait(200)

        else:
            print('continue in tournament page')
            self.Window.p1_label.setVisible(True)
            self.Window.p2_label.setVisible(True)
            self.Window.x_label.setVisible(True)
            self.Window.winner_label.setVisible(False)
            self.Window.start_button.setVisible(True)
            print('tournament_page : set players')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TournamentMain()
    w.show()
    sys.exit(app.exec_())
