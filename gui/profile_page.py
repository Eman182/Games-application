from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog

from backend_layer.facade import Facade
import gui
import params


class ProfileWindow(QWidget):

    def __init__(self, parent=None):
        super(ProfileWindow, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(1920, 1020)
        '''font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.setFont(font)'''
        self.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-space-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # ##########################################################################################################

        self.title_label = self.get_title_label()
        self.profile_pic = self.get_profile_pic()
        self.username_label = self.get_username_label()
        self.change_pic_button = self.get_change_pic_button()
        self.achievements_button = self.get_achievements_button()
        self.stats_label = self.get_stats_label()
        self.name_lineEdit = self.get_name_lineEdit()
        self.old_pw_lineEdit = self.get_old_pw_lineEdit()
        self.new_pw_lineEdit = self.get_new_pw_lineEdit()
        self.editname_button = self.get_editname_button()
        self.invalid_name_label = self.get_invalid_name_label()
        self.change_pw_button = self.get_change_pw_button()
        self.old_pw_label = self.get_old_pw_label()
        self.new_pw_label = self.get_new_pw_label()
        self.frame = self.get_frame()
        self.wins_label = self.get_wins_label()
        self.games_label = self.get_games_label()
        self.daily_ch_label = self.get_daily_ch_label()
        self.weekly_xp_label = self.get_weekly_xp_label()
        self.wins_num_label = self.get_wins_num_label()
        self.games_num_label = self.get_games_num_label()
        self.daily_num_ch_label = self.get_daily_ch_num_label()
        self.weekly_num_xp_label = self.get_weekly_xp_num_label()
        self.invalid_pic_label = self.get_invalid_pic_label()
        self.back_button = self.get_back_button()

        # ####################################################################

        # self.label_4.raise_()
        self.title_label.raise_()
        self.profile_pic.raise_()
        self.username_label.raise_()
        self.change_pic_button.raise_()
        self.stats_label.raise_()
        self.name_lineEdit.raise_()
        self.editname_button.raise_()
        self.invalid_name_label.raise_()
        self.change_pw_button.raise_()
        self.frame.raise_()
        self.invalid_pic_label.raise_()
        self.back_button.raise_()

        # self.retranslateUi(self)

        self.editname_button.clicked.connect(self.name_lineEdit.showNormal)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_title_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(700, 40, 631, 81))
        label.setFont(params.get_font(36))
        label.setStyleSheet(params.profile_title_style)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("Player\'s Profile")
        label.setObjectName("profile_title_label")
        return label

    def get_profile_pic(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(90, 220, 251, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)
        label.setMinimumSize(QtCore.QSize(251, 231))
        label.setStyleSheet(params.profile_pic_style)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setIndent(5)
        label.setText("profile image")
        label.setObjectName("profile_pic_label")
        return label

    def get_username_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(450, 250, 251, 41))
        label.setFont(params.get_font(22))
        label.setStyleSheet(params.profile_label_style)
        label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setText("User Name:")
        label.setObjectName("username_label")
        return label

    def get_old_pw_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(700, 340, 180, 40))
        label.setFont(params.get_font(13))
        label.setStyleSheet(params.profile_label_style)
        label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setText("old password:")
        label.setObjectName("old_pw_label")
        return label

    def get_new_pw_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(1250, 340, 180, 40))
        label.setFont(params.get_font(13))
        label.setStyleSheet(params.profile_label_style)
        label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setText("new password:")
        label.setObjectName("new_pw_label")
        return label

    def get_change_pic_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(70, 510, 291, 41))
        button.setFont(params.get_font(13, 40, True))
        button.setStyleSheet(params.profile_change_pic_style)
        button.setAutoDefault(False)
        button.setDefault(False)
        button.setFlat(False)
        button.setText("Change Profile Picture")
        button.setObjectName("change_pic_pushButton")
        button.clicked.connect(self.set_profile_pic)
        return button

    def get_achievements_button(self):
        achievementbtn = QtWidgets.QPushButton(self)
        achievementbtn.setGeometry(QtCore.QRect(850, 850, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        achievementbtn.setFont(font)
        achievementbtn.setStyleSheet("QPushButton{\n"
                                     "background-color:rgba(245, 98, 3,0.9);\n"
                                     "border-radius:25px;\n"
                                     "color:white;}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #e87c35;\n"
                                     "}")
        achievementbtn.setObjectName("achievementbtn")
        achievementbtn.setText("Achievements")
        achievementbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return achievementbtn

    def get_stats_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(450, 410, 201, 41))
        label.setFont(params.get_font(22))
        label.setStyleSheet(params.profile_label_style)
        label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setObjectName("stats_label")
        label.setText("Stats:")
        return label

    def get_name_lineEdit(self):
        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(730, 240, 341, 61))
        lineEdit.setFont(params.get_font(20, 50))
        lineEdit.setStyleSheet(params.profile_name_lineEdit_disabled)
        lineEdit.setInputMask("")
        lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        lineEdit.setObjectName("name_lineEdit")
        lineEdit.setText("Player\'s name")
        lineEdit.setDisabled(True)
        return lineEdit

    def get_old_pw_lineEdit(self):
        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(900, 340, 300, 45))
        lineEdit.setFont(params.get_font(20, 50))
        lineEdit.setStyleSheet(params.profile_name_lineEdit_enabled)
        lineEdit.setInputMask("")
        lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        lineEdit.setObjectName("old_pw_lineEdit")
        lineEdit.setText("")
        lineEdit.setEnabled(True)
        return lineEdit

    def get_new_pw_lineEdit(self):
        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(1450, 340, 300, 45))
        lineEdit.setFont(params.get_font(20, 50))
        lineEdit.setStyleSheet(params.profile_name_lineEdit_enabled)
        lineEdit.setInputMask("")
        lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        lineEdit.setObjectName("new_pw_lineEdit")
        lineEdit.setText("")
        lineEdit.setEnabled(True)
        return lineEdit

    def get_editname_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(1130, 250, 71, 41))
        button.setFont(params.get_font(13, 62, True, False))
        button.setStyleSheet(params.profile_button_style)
        button.setObjectName("editname_pushButton")
        button.setText("Edit")
        button.clicked.connect(self.toggle_field)
        return button

    def get_invalid_name_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(1240, 250, 260, 31))
        label.setFont(params.get_font(10, 62, True))
        label.setStyleSheet(params.invalid_style)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("User Name already exists")
        label.setObjectName("invalid_name_label")
        label.setVisible(False)
        return label

    def get_change_pw_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(445, 340, 230, 50))
        button.setStyleSheet(params.profile_button_style)
        button.setObjectName("change_pw_pushButton")
        button.setText("Change password")
        button.setFont(params.get_font(13))
        button.clicked.connect(self.toggle_change_pw)
        return button

    def get_frame(self):
        frame = QtWidgets.QFrame(self)
        frame.setGeometry(QtCore.QRect(550, 480, 721, 341))
        frame.setStyleSheet(params.profile_frame_style)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        return frame

    def get_wins_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(40, 20, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_stats_label_style)
        label.setText("  number of wins : ")
        label.setObjectName("wins_label")
        return label

    def get_games_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(40, 90, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_stats_label_style)
        label.setText("  number of games : ")
        label.setObjectName("games_label")
        return label

    def get_daily_ch_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(40, 160, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_stats_label_style)
        label.setText("  daily challenges : ")
        label.setObjectName("daily_ch_label")
        return label

    def get_weekly_xp_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(40, 230, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_stats_label_style)
        label.setObjectName("weekly_xp_label")
        label.setText("  this week's xp : ")
        return label

    def get_wins_num_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(170, 20, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_num_label_style)
        label.setText("  a number ")
        label.setObjectName("wins_num_label")
        return label

    def get_games_num_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(170, 90, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_num_label_style)
        label.setObjectName("games_num_label")
        label.setText("  a number ")
        return label

    def get_daily_ch_num_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(170, 160, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_num_label_style)
        label.setObjectName("daily_ch_num_label")
        label.setText("  a number ")
        return label

    def get_weekly_xp_num_label(self):
        label = QtWidgets.QLabel(self.frame)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(170, 230, 250, 35))
        label.setFont(params.get_font(11))
        label.setStyleSheet(params.profile_num_label_style)
        label.setObjectName("weekly_xp_num_label")
        label.setText("  a number ")
        return label

    def get_invalid_pic_label(self):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(560, 550, 220, 41))
        label.setFont(params.get_font(10, 62, True))
        label.setStyleSheet(params.invalid_style)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("Can't set profile picture")
        label.setObjectName("invalid_pic_label")
        label.setVisible(False)
        return label

    def get_back_button(self):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(40, 870, 80, 80))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(params.back_button_style)
        button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../storage/Icons/back.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        button.setIcon(icon1)
        button.setIconSize(QtCore.QSize(50, 50))
        button.setObjectName("back_pushButton")
        return button

    def set_profile_pic(self):
        self.invalid_pic_label.setVisible(False)
        fname = QFileDialog.getOpenFileName(self, "Open file", "c:\\", "Image files (*.jpg *.jpeg *.png)")
        image_path = fname[0]
        # print("image path : ", image_path, "**", len(image_path))
        if len(image_path) == 0:  # no pic chosen
            return

        print("create facade in get image")
        f = Facade.get_instance()
        print("facade instance created")
        check, new_path = f.change_profile_pic(image_path)
        if check:
            pixmap = QPixmap(new_path)
            self.profile_pic.setPixmap(QPixmap(pixmap))
            self.profile_pic.setScaledContents(True)
            # gui.player_global.set_avatar(image_path)
        else:
            self.invalid_pic_label.setVisible(True)

    def save_name(self):
        self.invalid_name_label.setVisible(False)
        print(self.name_lineEdit.text())
        f = Facade.get_instance()
        # gui.player_global.set_name(self.name_lineEdit.text())
        if f.save_name(self.name_lineEdit.text()):
            self.editname_button.setText("Edit")
            self.name_lineEdit.setStyleSheet(params.profile_name_lineEdit_disabled)
            self.name_lineEdit.setDisabled(True)
        else:
            self.invalid_name_label.setVisible(True)


    def enable_name(self):
        print("edit name")
        self.editname_button.setText("Save")
        self.name_lineEdit.setStyleSheet(params.profile_name_lineEdit_enabled)
        self.name_lineEdit.setEnabled(True)
        self.name_lineEdit.setFocus(True)

    def toggle_field(self):
        if self.name_lineEdit.isEnabled():  # button is active now and we need to save changes
            self.save_name()
        else:  # button is disabled and we need to make changes
            self.enable_name()

    def save_pw(self):
        f = Facade.get_instance()
        old, new = self.old_pw_lineEdit.text(), self.new_pw_lineEdit.text()
        if f.save_password(old, new):
            self.change_pw_button.setText("Change password")
            self.old_pw_lineEdit.setVisible(False)
            self.new_pw_lineEdit.setVisible(False)
            self.old_pw_label.setVisible(False)
            self.new_pw_label.setVisible(False)
        else:
            pass

    def enable_change_pw(self):
        self.change_pw_button.setText("Save password")
        self.old_pw_lineEdit.setVisible(True)
        self.new_pw_lineEdit.setVisible(True)
        self.old_pw_label.setVisible(True)
        self.new_pw_label.setVisible(True)

    def toggle_change_pw(self):
        if self.old_pw_lineEdit.isVisible() or self.new_pw_lineEdit.isVisible():
            self.save_pw()
        else:
            self.enable_change_pw()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.save_name()

    '''def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "profile"))
        # self.label.setText(_translate("Form", "Player\'s Profile"))
        # self.label_2.setText(_translate("Form", "profile image"))
        # self.label_5.setText(_translate("Form", "User Name:"))
        # self.pushButton.setText(_translate("Form", "Change Profile Picture"))
        # self.stats_label.setText(_translate("Form", "Stats:"))
        # self.lineEdit.setText(_translate("Form", "Player\'s name"))
        # self.lineEdit.setDisabled(True)
        # self.editname_button.setText(_translate("Form", "Edit"))
        # self.editname_button.clicked.connect(self.toggle_field)

        # self.label_6.setText(_translate("Form", "User Name already exists"))
        # self.label_6.setVisible(False)
        # self.change_pw_button.setText(_translate("Form", "Change password"))
        # self.wins_label.setText(_translate("Form", "  number of wins : "))
        #self.games_label.setText(_translate("Form", "  number of games : "))
        #self.daily_ch_label.setText(_translate("Form", "  daily challenges : "))
        #self.weekly_xp_label.setText(_translate("Form", "  this week's xp : "))
        # self.wins_num_label.setText(_translate("Form", "  a number "))
        #self.label_13.setText(_translate("Form", "  a number "))
        #self.label_14.setText(_translate("Form", "  a number "))
        #self.label_15.setText(_translate("Form", "  a number "))'''


class ProfileMain(QMainWindow):
    def __init__(self, parent=None):
        super(ProfileMain, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(1920, 1080)
        self.startUIWindow()
        self.movie = QMovie("../storage/BackGround/user.jpg")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = ProfileWindow(self)
        self.setWindowTitle("My Program")

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def refresh(self):
        self.Window.name_lineEdit.setText(gui.player_global.get_name())
        self.Window.name_lineEdit.setDisabled(True)
        self.Window.name_lineEdit.setStyleSheet(params.profile_name_lineEdit_disabled)
        self.Window.invalid_name_label.setVisible(False)
        self.Window.editname_button.setText("Edit")
        print(gui.player_global.get_name(), gui.player_global.get_wins(), gui.player_global.get_games(), gui.player_global.get_daily_challenges(), gui.player_global.get_weekly_xp())
        self.Window.wins_num_label.setText(str(gui.player_global.get_wins()))
        self.Window.games_num_label.setText(str(gui.player_global.get_games()))
        self.Window.daily_num_ch_label.setText(str(gui.player_global.get_daily_challenges()))
        self.Window.weekly_num_xp_label.setText(str(gui.player_global.get_weekly_xp()))
        pixmap = QPixmap(gui.player_global.get_avatar())
        self.Window.profile_pic.setPixmap(QPixmap(pixmap))
        self.Window.profile_pic.setScaledContents(True)
        self.Window.old_pw_lineEdit.setVisible(False)
        self.Window.new_pw_lineEdit.setVisible(False)
        self.Window.old_pw_label.setVisible(False)
        self.Window.new_pw_label.setVisible(False)
