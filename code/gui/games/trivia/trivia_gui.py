from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap, QCursor, QPainter, QMovie, QIcon
from PyQt5 import QtCore, QtTest
from urllib.request import urlopen
import json
import pandas as pd
import random
import ssl

from gui.params import start_bcg

ssl._create_default_https_context = ssl._create_unverified_context
# open api link to database
with urlopen("https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple") as webpage:
    # read JSON file & extract data
    data = json.loads(webpage.read().decode())
    df = pd.DataFrame(data["results"])


# load 1 instance of questions & answers at a time from the database
def preload_data(idx):
    # idx parm: selected randomly time and again at function call
    question = df["question"][idx]
    correct = df["correct_answer"][idx]
    wrong = df["incorrect_answers"][idx]

    # fixing charecters with bad formatting
    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "<"),
        ("&gt;", ">")
    ]

    # replace bad charecters in strings
    for tuple in formatting:
        question = question.replace(tuple[0], tuple[1])
        correct = correct.replace(tuple[0], tuple[1])
    # replace bad charecters in lists
    for tuple in formatting:
        wrong = [char.replace(tuple[0], tuple[1]) for char in wrong]

    # store local values globally
    parameters["question"].append(question)
    parameters["correct"].append(correct)

    all_answers = wrong + [correct]
    random.shuffle(all_answers)

    parameters["answer1"].append(all_answers[0])
    parameters["answer2"].append(all_answers[1])
    parameters["answer3"].append(all_answers[2])
    parameters["answer4"].append(all_answers[3])

    # print correct answer to the terminal (for testing)
    print(parameters["correct"][-1])


# dictionary to store local pre-load parameters on a global level
parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [],
    "score2": [],
    "mode": [],
    "turn": [],
    "index": [],
    "num": []
}

# global dictionary of dynamically changing widgets
widgets = {
    "lab": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "message": [],
    "message2": [],
    "turn": [],
    "qbtn": []
}

game_player1 = None
game_player2 = None
quit_button = None

# initialliza grid layout
grid = QGridLayout()


def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
            widgets[widget][0].hide()
        for i in range(0, len(widgets[widget])):
            if widget != "qbtn":
                widgets[widget].pop()


def clear_parameters():
    # clear the global dictionary of parameters
    for parm in parameters:
        if parameters[parm] != []:
            for i in range(0, len(parameters[parm])):
                parameters[parm].pop()
    # populate with initial index & score values
    parameters["index"].append(random.randint(0, 49))
    parameters["score"].append(0)
    parameters["score2"].append(0)
    parameters["num"].append(0)


def start_game(mode):
    # start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    parameters["mode"].append(mode)
    parameters["turn"].append(1)
    preload_data(parameters["index"][-1])
    # display the game frame
    frame2()


def create_buttons(answer, l_margin, r_margin):
    # create identical buttons with custom left & right margins
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setGeometry(QtCore.QRect(480 + l_margin, 530 + r_margin, 350, 51))
    button.setStyleSheet(
        # setting variable margins
        '''*{
        border: 4px solid '#ff5f00';
        color: white;
        font-family: 'shanti';
        font-size: 20px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px;
        }
        *:hover{
            background: '#ff5f00';
        }
        "QPushButton:focus {\n"\
        "outline: none;box-shadow: none;\n}" 
        '''
    )
    button.clicked.connect(lambda x: is_correct(button))
    return button


def is_correct(btn):
    if parameters["mode"][-1] == 1:
        mode1(btn)
    else:
        print("in is correct")
        mode2(btn)


def mode1(btn):
    temp_num = parameters["num"][-1]
    parameters["num"].pop()
    parameters["num"].append(temp_num + 1)
    # CORRECT ANSWER
    if btn.text() == parameters["correct"][-1]:
        # update score (+10 points)
        btn.setStyleSheet(
            '''*{
            color: white;
            font-family: 'shanti';
            font-size: 20px;
            border-radius: 25px;
            padding: 15px 0;
            margin-top: 20px;
            background: 'green';
            }
            "QPushButton:focus {\n"\
            "outline: none;box-shadow: none;\n}" 
            '''
        )
        temp_score = parameters["score"][-1]
        parameters["score"].pop()
        parameters["score"].append(temp_score + 10)
    else:
        btn.setStyleSheet(
            '''*{
            color: white;
            font-family: 'shanti';
            font-size: 20px;
            border-radius: 25px;
            padding: 15px 0;
            margin-top: 20px;
            background: 'red';
            }
            "QPushButton:focus {\n" \
            "outline: none;box-shadow: none;\n}"
            '''
        )

    # select a new random index and replace the old one
    parameters["index"].pop()
    parameters["index"].append(random.randint(0, 49))
    # preload data for new index value
    preload_data(parameters["index"][-1])

    # update the text of all widgets with new data
    QtTest.QTest.qWait(500)
    btn.setStyleSheet(
        '''*{
        border: 4px solid '#ff5f00';
        color: white;
        font-family: 'shanti';
        font-size: 20px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px; 
        }
        *:hover{
            background: '#ff5f00';
        }
        "QPushButton:focus {\n"\
        "outline: none;box-shadow: none;\n}" 
        '''
    )
    widgets["score"][-1].setText(str(parameters["score"][-1]))
    widgets["question"][0].setText(parameters["question"][-1])
    widgets["answer1"][0].setText(parameters["answer1"][-1])
    widgets["answer2"][0].setText(parameters["answer2"][-1])
    widgets["answer3"][0].setText(parameters["answer3"][-1])
    widgets["answer4"][0].setText(parameters["answer4"][-1])

    if parameters["num"][-1] >= 10:
        # WON THE GAME
        clear_widgets()
        frame3()


def mode2(btn):
    temp_num = parameters["num"][-1]
    parameters["num"].pop()
    parameters["num"].append(temp_num + 1)
    # swap turns
    if parameters["turn"][-1] == 1:
        check = "score"
        swap = "score2"
        parameters["turn"].pop()
        parameters["turn"].append(2)
    else:
        check = "score2"
        swap = "score"
        parameters["turn"].pop()
        parameters["turn"].append(1)

    # CORRECT ANSWER
    if btn.text() == parameters["correct"][-1]:
        # update score (+10 points)
        btn.setStyleSheet(
            '''*{
            color: white;
            font-family: 'shanti';
            font-size: 20px;
            border-radius: 25px;
            padding: 15px 0;
            margin-top: 20px;
            background: 'green';
            }
            '''
            "QPushButton:focus {\n" \
            "outline: none;box-shadow: none;\n}"
        )
        temp_score = parameters[check][-1]
        parameters[check].pop()
        parameters[check].append(temp_score + 10)
    else:
        btn.setStyleSheet(
            '''*{
            color: white;
            font-family: 'shanti';
            font-size: 20px;
            border-radius: 25px;
            padding: 15px 0;
            margin-top: 20px;
            background: 'red';
            }
            '''
            "QPushButton:focus {\n" \
            "outline: none;box-shadow: none;\n}"
        )

    # select a new random index and replace the old one
    parameters["index"].pop()
    parameters["index"].append(random.randint(0, 49))
    # preload data for new index value
    preload_data(parameters["index"][-1])
    QtTest.QTest.qWait(500)
    # update the text of all widgets with new data
    btn.setStyleSheet(
        '''*{
        border: 4px solid '#ff5f00';
        color: white;
        font-family: 'shanti';
        font-size: 20px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px; 
        }
        *:hover{
            background: '#ff5f00';
        }
        "QPushButton:focus {\n"\
        "outline: none;box-shadow: none;\n}" 
        '''
    )
    widgets["score"][-1].setText(str(parameters[swap][-1]))
    widgets["turn"][-1].setText("Player" + str(parameters["turn"][-1]))
    if game_player1 is not None and game_player2 is not None:
        names = [game_player1.get_name(), game_player2.get_name()]
        print(names[parameters["turn"][-1] - 1])
        widgets["turn"][-1].setText(names[parameters["turn"][-1] - 1])

    widgets["question"][0].setText(parameters["question"][-1])
    widgets["answer1"][0].setText(parameters["answer1"][-1])
    widgets["answer2"][0].setText(parameters["answer2"][-1])
    widgets["answer3"][0].setText(parameters["answer3"][-1])
    widgets["answer4"][0].setText(parameters["answer4"][-1])

    if parameters["num"][-1] >= 10:
        # WON THE GAME
        clear_widgets()
        frame3()


# *********************************************
#                  FRAME 1
# *********************************************
def set_style(name):
    button = QPushButton(name)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#ff5f00';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: auto;
            display: flex;
            display: grid;   
        }
        *:hover{
            background: '#ff5f00';
        }
        "QPushButton:focus {\n"\
        "outline: none;box-shadow: none;\n}" 
        '''
    )
    return button


def frame1(quitbtn):
    clear_widgets()
    logo = QLabel()
    logo.setText("Start game")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        '''
    *{
        margin-top: 200px;
        font-size: 100px;
        color: 'white';
    }'''
    )
    widgets["lab"].append(logo)

    button1 = set_style("1 Player")
    button2 = set_style("2 Players")

    # button callback
    button1.clicked.connect(lambda x: start_game(1))
    button2.clicked.connect(lambda x: start_game(2))
    widgets["button"].append(button1)
    widgets["button"].append(button2)
    widgets["qbtn"].append(quitbtn)
    # place global widgets on the grid
    grid.addWidget(widgets["lab"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][0], 1, 0, 3, 2)
    grid.addWidget(widgets["button"][-1], 2, 0, 3, 2)
    grid.addWidget(widgets["qbtn"][-1], 4, 0)
    widgets["qbtn"][-1].show()


# *********************************************
#                  FRAME 2
# *********************************************

def frame2():
    # score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignCenter)
    score.setStyleSheet(
        '''
        font-size: 35px;
        color: 'white';
        padding: 15px 10px;
        margin: 100px 200px;
        background: '#64A314';
        border: 1px solid '#64A314';
        border-radius: 35px;
        '''
    )
    widgets["score"].append(score)

    turn = QLabel("Player " + str(parameters["turn"][-1]))
    turn.setAlignment(QtCore.Qt.AlignCenter)
    turn.setStyleSheet(
        '''
        font-size: 50px;
        color: 'white';
        padding: 15px 10px;
        margin: 100px 200px;
        '''
    )

    # question widget
    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 75px;
        '''
    )
    widgets["question"].append(question)

    # answer button widgets
    button1 = create_buttons(parameters["answer1"][-1], 85, 5)
    button2 = create_buttons(parameters["answer2"][-1], 5, 85)
    button3 = create_buttons(parameters["answer3"][-1], 85, 5)
    button4 = create_buttons(parameters["answer4"][-1], 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    # place widget on the grid
    if parameters["mode"][-1] == 2:
        if game_player1 is not None and game_player2 is not None:
            names = [game_player1.get_name(), game_player2.get_name()]
            print(names[parameters["turn"][-1]-1])
            turn.setText(names[parameters["turn"][-1]-1])

        widgets["turn"].append(turn)
        grid.addWidget(widgets["turn"][-1], 0, 0)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)


# *********************************************
#             FRAME 3 - WIN GAME
# *********************************************

def quit():
    print('inside quit +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    global game_player1, game_player2
    print("players : ", game_player1, game_player2)
    print(game_player1.get_name())
    is_win1, is_win2 = 0, 0
    gained1, gained2 = 0, 0
    if parameters["mode"][-1] == 1 and game_player1 is not None:
        print('condition 1')
        gained1 = parameters["score"][-1] // 5
        if parameters["score"][-1] == 100:
            is_win1 = 1
            gained1 = gained1 + 5
        game_player1.report_game(is_win1, gained1)
        print("xp1 " + str(game_player1.get_xp()))
    elif parameters["mode"][-1] == 2 and game_player1 is not None and game_player2 is not None:
        print('condition 2')
        gained1 = parameters["score"][-1] // 5
        gained2 = parameters["score2"][-1] // 5
        game_player1.report_game(is_win1, gained1)
        game_player2.report_game(is_win2, gained2)
        # print("win1 " + str(game_player1.get_wins()))
        print("xp1 " + str(game_player1.get_xp()))
        # print("win2 " + str(game_player2.get_wins()))
        print("xp2 " + str(game_player2.get_xp()))
        print('quit button', quit_button)
        widgets["qbtn"][-1].click()
        print('finish')
        return

    frame1(widgets["qbtn"][-1])
    print('after quit +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


def frame3():
    # congradulations widget
    if parameters["mode"][-1] == 1:
        message = QLabel("Congratulations!\n your score is:")
    else:
        if parameters["score"][-1] > parameters["score2"][-1]:
            message = QLabel("The winner is player1 \nThe results are:")
            if game_player1 is not None and game_player2 is not None:
                message.setText(f"The winner is {game_player1.get_name()} \nThe results are:")
        elif parameters["score"][-1] < parameters["score2"][-1]:
            message = QLabel("The winner is player2 \nThe  results are:")
            if game_player1 is not None and game_player2 is not None:
                message.setText(f"The winner is {game_player2.get_name()} \nThe results are:")
        else:
            message = QLabel("Tie \nThe  results are:")

    message.setAlignment(QtCore.Qt.AlignCenter)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 50px; color: 'white'; margin: 150px 0px;"
    )
    widgets["message"].append(message)

    # score widget
    if parameters["mode"][-1] == 1:
        score = QLabel(str(parameters["score"][-1]))
        score.setStyleSheet("font-size: 100px; color: #8FC740; margin: 0 75px 0px 75px;")
        widgets["score"].append(score)
    else:
        score = QLabel(str(parameters["score"][-1]) + " : " + str(parameters["score2"][-1]))
        score.setStyleSheet("font-size: 100px; color: #8FC740; margin: 0 75px 0px 75px;")
        widgets["score"].append(score)

    # go back to work widget
    message2 = QLabel("OK. That was fun.")
    message2.setAlignment(QtCore.Qt.AlignCenter)
    message2.setStyleSheet(
        "font-family: 'Shanti'; font-size: 30px; color: 'OrangeRed'; margin-top:0px; margin-bottom:75px;"
    )
    widgets["message2"].append(message2)

    # button widget
    button = QPushButton('Quit')
    button.setStyleSheet(
        "*{background:'#ff5f00'; padding:25px 0px; border: 1px solid '#BC006C'; color: 'white'; font-family: 'Arial'; "
        "font-size: 25px; border-radius: 40px; margin: 10px 100px; margin-bottom: 100px;} *:hover{"
        "background:'#ff5f00';}"
        "QPushButton:focus {\n" \
        "outline: none;box-shadow: none;\n}"
    )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(quit)

    widgets["button"].append(button)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)


class StartGameMain(QMainWindow):
    def __init__(self, parent=None):
        super(StartGameMain, self).__init__(parent)
        self.Window = QWidget()
        self.Window.setWindowTitle("Trivia game")
        self.Window.show()
        self.Window.setStyleSheet("background: #161219;")
        # display frame 1
        self.quitbtn = self.init_quitbtn()
        global quit_button
        quit_button = self.quitbtn

        frame1(self.quitbtn)

        self.Window.setLayout(grid)
        self.movie = QMovie(start_bcg)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def set_player(self, player1, player2=None):
        global game_player1, game_player2
        game_player1 = player1
        game_player2 = player2

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def init_quitbtn(self):
        quit_btn = QPushButton(self)
        quit_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        quit_btn.setStyleSheet("QPushButton{\n"
                               "background:transparent;\n"
                               "border-radius: 35px;\n"
                               "text-align: left;\n"
                               "padding-left: 25px;"
                               "}\n"
                               "QPushButton:focus {\n" \
                               "outline: none;box-shadow: none;\n}"
                               )
        quit_btn.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("../storage/Icons/sign-out.png"), QIcon.Normal, QIcon.Off)
        quit_btn.setIcon(icon1)
        quit_btn.setIconSize(QtCore.QSize(80, 80))
        quit_btn.setObjectName("quit_btn")
        return quit_btn


    def refresh(self):
        clear_parameters()
        global game_player1, game_player2, quit_button
        game_player1 = None
        game_player2 = None
        quit_button = None
        frame1(self.quitbtn)
