import sys
import time
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QMovie, QPainter
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar, QLabel, QLineEdit

'''
old gamespace variables
label3: name
label4: level
label2: avatar
label5
label6 game
pushbutton go to profile
push3 exit

'''
'''
old start page variables
push2 sign in
push sign up
push 3 guest
label 2 title
label


'''


def init_font_landing():
    font = QtGui.QFont()
    font.setFamily("Papyrus")
    font.setPointSize(15)
    font.setBold(True)
    font.setWeight(95)
    font.setStrikeOut(False)
    return font


def init_font_start(size, isItalic):
    font = QtGui.QFont()
    font.setFamily("OCR A Extended")
    font.setPointSize(size)
    font.setBold(True)
    font.setItalic(isItalic)
    font.setWeight(75)
    return font


def get_font(size, weight=40, is_bold=False, is_italic=False):
    font = QtGui.QFont()
    font.setFamily("OCR A Extended")
    font.setPointSize(size)
    font.setWeight(weight)
    font.setBold(is_bold)
    font.setItalic(is_italic)
    return font


sign_in_lineEdit_style = "QLineEdit{\nbackground-color: rgba(230, 230, 230,0.6) ;\nborder: 5px solid rgba(0,0,0," \
                         "0) ;\nborder-radius:4px ;\nborder-bottom-color:rgba(46,82,101,200) ;\ncolor: #14279B " \
                         ";\npadding-bottom:7px ;\n} "

background_style = "background-image:url(:/newPrefix/f.jpg);\nbackground-repeat: no-repeat;\nbackground-size: " \
                   "contain, cover; "

back_button_style = "QPushButton{\nbackground-color:rgba(152,186,231,0.7);\nborder-radius: " \
                    "40px;\n}\nQPushButton:hover{\nbackground-color:#98BAE7;\n}" \
                    "QPushButton:focus {\n"\
                    "outline: none;box-shadow: none;\n}"

show_password_button_style = "background-color: transparent;\nbackground:none;\nborder: none;"

next_button_style = "QPushButton {\nbackground:linear-gradient(to bottom, #599bb3 5%, #408c99 " \
                    "100%);\nbackground-color:#E6E6E6;\nborder-radius:8px;\nborder:1px solid " \
                    "#d6bcd6;\ncolor:#3a8a9e;\ntext-decoration:none;\ntext-shadow:0px 1px 0px " \
                    "#e1e2ed;\n}\nQPushButton:hover {\nbackground:linear-gradient(to bottom, #bab1ba 5%, " \
                    "#ededed 100%);\nbackground-color:#bab1ba;\n}\nQPushButton:active {" \
                    "\nposition:relative;\ntop:1px;\n} "

invalid_style = "QLabel{\ncolor:rgb(255,69,72);\n}"

# sizes
# land page

landing_width = 720
landing_height = 1000
land_page_progressbar_size = QRect(230, 850, 261, 30)

# gamespace
gamespace_width = 1920
gamespace_height = 1080

# backgrounds
landing_bcg = "../storage/BackGround/landing_page.gif"
gamespace_bcg = "../storage/BackGround/gamespace.jpg"
start_bcg = "../storage/BackGround/start.jpg"
startG_bcg = "../storage/BackGround/gamespace.jpg"

# sound
sound = "../storage/Sounds/mixkit-small-hit-in-a-game-2072.wav"

# fonts
font_landing = init_font_landing()

# style sheets
progressbar_landing_sheet = ("QProgressBar\n"
                             "{\n"
                             "    background:rgba(255, 255, 255,0.5);\n"
                             "    border-radius : 15px;\n"
                             "text-align: center;\n"

                             "\n"
                             "}\n"
                             "QProgressBar::chunk \n"
                             "{\n"
                             "background:rgb(110, 60,188,0.5);\n"

                             "border-radius :15px;\n"
                             "border:3px solid;\n"

                             "border-color:    rgba(255, 255, 255,0.5);\n"
                             "} ")
quote_sheet = ("border-radius:15px;\n"
               "background:rgba(255, 255, 255,0.2);\n")
level_progress_sheet = ("QProgressBar:horizontal {\n"
                        "border: 1px solid gray;\n"
                        "border-radius: 3px;\n"
                        "background: white;\n"
                        "padding: 3px;\n"
                        "text-align: center;\n"
                        "margin-right: 4ex;\n"
                        "}\n"
                        "QProgressBar::chunk:horizontal {\n"
                        "background:rgb(241, 236, 83);\n"
                        "width: 10px;\n"
                        "\n"
                        "}")
startpg_buttons_sheet = ("QPushButton{\n"
                         "    box-shadow: -1px 0px 6px 0px #F0D9FF;\n"
                         "    background-color:#6E3CBC;\n"
                         "    border-radius:38px;\n"
                         "    border:4px solid #F0D9FF;\n"
                         "    cursor:pointer;\n"
                         "    color:#ffffff;\n"
                         "    font-size:26px;\n"
                         "    font-family:OCR A Extended;\n"
                         "    font-style:italic;\n"
                         "    font-weight:bold;\n"
                         "    padding:22px 15px;\n"
                         "}\n"
                         "QPushButton:hover {\n"
                         "    background-color:#BFA2DB;\n"
                         "}")
startG_buttons_sheet = ("QPushButton{\n"
                         "    box-shadow: -1px 0px 6px 0px #F0D9FF;\n"
                         "    background-color:#98BAE7;\n"
                         "    border-radius:38px;\n"
                         "    border:4px solid #F0D9FF;\n"
                         "    cursor:pointer;\n"
                         "    color:#14279B;\n"
                         "    font-size:30px;\n"
                         "    font-family:OCR A Extended;\n"
                         "    font-style:italic;\n"
                         "    font-weight:bold;\n"
                         "    padding:22px 15px;\n"
                         "}\n"
                         "QPushButton:hover {\n"
                         "    background-color:#F14A16;\n"
                        "color: #E6E6E6;\n"
                         "}")
landing_title = "Black Hole"
gamespace_title = "Home"
startpage_title = "Welcome Alien"

profile_title_style = "border-left: 10px solid  rgb(255, 255, 255);\nbackground-color: rgba(184, 228, 240," \
                      "0.3);\ncolor: rgb(255, 255, 255); "

profile_pic_style = "border-radius: 7px;\nbackground-color: rgba(0, 0, 49,0.6);\nborder : 2px groove rgb(157, 158, " \
                    "253);\n "

profile_change_pic_style = "QPushButton{\n" \
                           "color:rgb(248, 255, 105);\n" \
                           "font: 11pt \"OCR A Extended\";\n" \
                           "border-radius: 1px;\n" \
                           "border-bottom: 4px solid rgba(152, 186, 231,0);\n" \
                           "font-weight: 500;}\n" \
                           "QPushButton:hover{\n" \
                           "color: rgb(9, 6, 75);\n" \
                           "background-color: rgba(152, 186, 231,0.7);\n" \
                           "border-bottom: 4px solid rgb(152, 186, 231);\n" \
                           "font: 11pt \"OCR A Extended\";\n" \
                           "box-sizing: border-box;\n" \
                           "font-weight: 500;\n}"

profile_label_style = "color: rgb(255, 255, 255);\n" \
                      "border-left: 5px solid  rgb(255, 255, 255);\n" \
                      "border-radius : 10px;\n"

profile_name_lineEdit_disabled = "QLineEdit{\n" \
                                 "    color: rgb(255, 255, 255);\n" \
                                 "    background-color: rgba(230, 230, 230,0) ;\n" \
                                 "    font: 20pt \"OCR A Extended\";\n" \
                                 "    border-radius: 1px;\n" \
                                 "    border-bottom: 5px solid rgba(255,255,255,0);\n" \
                                 "}\n" \
                                 "QLineEdit:focus{\n" \
                                 "    background-color: rgba(230, 230, 230,0.6) ;\n" \
                                 "    border-bottom: 5px solid rgba(255,255,255,1);\n" \
                                 "}\n"

profile_name_lineEdit_enabled = "    color: rgb(255, 255, 255);\n" \
                                "    font: 20pt \"OCR A Extended\";\n" \
                                "    border-radius: 1px;\n" \
                                "    background-color: rgba(230, 230, 230,0.6) ;\n" \
                                "    border-bottom: 5px solid rgba(255,255,255,1);\n"

profile_button_style = "QPushButton{\n" \
                       "    color:rgb(248, 255, 105);\n" \
                       "    border-radius: 1px;\n" \
                       "    border-bottom: 4px solid rgba(152, 186, 231,0);\n" \
                       "    font-weight: 500;\n" \
                       "}\n" \
                       "QPushButton:hover{\n" \
                       "    color: rgb(9, 6, 75);\n" \
                       "    background-color: rgba(152, 186, 231,0.7);\n" \
                       "    border-bottom: 4px solid rgb(152, 186, 231);\n" \
                       "    box-sizing: border-box;\n" \
                       "    font-weight: 500;\n" \
                       "}"

profile_frame_style = "border-left : 7px solid rgb(255, 255, 255);\n" \
                      "background-color : rgba(184, 228, 240,0.3); "

profile_stats_label_style = "color: rgb(0, 13, 46);\n"\
                                   "border : none;\n"\
                                   "background:none;\n"\
                                   "font-size : 20px;\n"\
                                   "font-weight : 600;"

profile_num_label_style = "color: rgb(248, 255, 105);\n"\
                                    "border : none;\n"\
                                    "background:none;\n"\
                                    "font-size : 19px;\n"\
                                    "font-weight : 500;"
#leader board
leaderboard_tabel_style = "QTableWidget {background-color:transparent; font: 15pt \"OCR A Extended\"; border: none;}"\
            "QHeaderView {border:none; background-color:transparent; font: 25pt \"OCR A Extended\";}"\
            "QHeaderView::focus {border:none}"\
            "QHeaderView::section {background-color:transparent; border-bottom: 1px solid #ffffff; color: #ffffff}"\
            "QHeaderView::section::horizontal {background-color:rgba(127, 124, 130, 0.5);}"\
            "QTableCornerButton::section {background-color:rgba(127, 124, 130, 0.5);}"\
            "QTableView::item {border-bottom: 1px solid #ffffff; color: #ffffff; text-align: center;}"\
            "QTableView::item::hover{background-color:#BFA2DB; color:blue;}"

tournament_tabel_style = "QTableWidget {background-color:transparent; font: 15pt \"OCR A Extended\"; border: none;}"\
            "QHeaderView {border:none; background-color:transparent; font: 25pt \"OCR A Extended\";}"\
            "QHeaderView::focus {border:none}"\
            "QHeaderView::section {background-color:transparent; border-bottom: 1px solid #ffffff; color: #ffffff}"\
            "QHeaderView::section::horizontal {background-color:rgba(127, 124, 130, 0.5);}"\
            "QTableCornerButton::section {background-color:rgba(127, 124, 130, 0.5);}"\
            "QTableView::item {border-bottom: 1px solid #ffffff; text-align: center;}"\


leaderboard_frame_style = "background-color: rgba(110, 60, 188,0.4);  box-shadow: 20px 20px white; border-radius: 5px"
tournament_frame_style = "background-color: rgba(86, 127, 199,0.7);  box-shadow: 20px 20px white; border-radius: 5px"
tournament_player_label_style = "background-color: rgba(255, 255, 255, 0.5); border: 3px solid rgba(86, 127, 199,0.7); border-radius: 20px"
#6E3CBC
#d98adb

#achievements
achievment_table_style = ("    QTableWidget {\n"
                          "        background-color: transparent; \n"
                          "        border-radius: 10px; border:none\n"
                          "    }\n"
                          "\n"
                          "    QTableWidget::item {\n"
                          "        color:rgb(255, 255, 255);                    \n"
                          "        background-color: rgba(110, 60, 188,0.4);\n"
                          "        margin-top: 5px;          \n"
                          "        border-radius: 9px;\n"
                          "        padding-left: 5px;\n"
                          "    }\n"
                          "\n"
                          "    QTableWidget::item:hover {\n"
                          "        background-color: #BFA2DB;\n"
                          "        color: blue;\n"
                          "    }"
                          "QHeaderView {border:none; background-color:rgba(127, 124, 130, 0.5); font: 25pt \"OCR A Extended\";}"
                          "QHeaderView::focus {border:none}"
                          "QHeaderView::section {background-color:transparent; border-bottom: 1px solid #ffffff; color: #ffffff}"
                          "QHeaderView::section::horizontal {background-color:rgba(127, 124, 130, 0.5);}""")
scroll_style = (""" QScrollBar:vertical {
                                                                 border: 2px solid grey;
                                                                 background: transparent;
                                                                 width: 15px;
                                                                 margin: 22px 0 22px 0;
                                                             }
                                                             QScrollBar::handle:vertical {
                                                                 background: rgba(255,255,255,0.8);
                                                                 min-height: 20px;
                                                                 border-radius : 5% ;
                                                             }
                                                             QScrollBar::add-line:vertical {
                                                                 border: 2px solid grey;
                                                                 background: #BFA2DB;
                                                                 height: 20px;
                                                                 subcontrol-position: bottom;
                                                                 subcontrol-origin: margin;
                                                             }

                                                             QScrollBar::sub-line:vertical {
                                                                 border: 2px solid grey;
                                                                 background: #BFA2DB;
                                                                 height: 20px;
                                                                 subcontrol-position: top;
                                                                 subcontrol-origin: margin;
                                                             }
                                                             QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                                                 border: 2px solid grey;
                                                                 width: 3px;
                                                                 height: 3px;
                                                                 background: white;
                                                             }

                                                             QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                                                 background: none;
 }""")