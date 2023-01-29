from PyQt5.QtCore import QUrl, QEventLoop, QTimer, QElapsedTimer
from PyQt5.QtWidgets import QApplication
import sys
import signIn
import signUp
import gamespace
import start_page
import profile_page
import landing_page
import leaderboard
import achievements_page
from PyQt5 import QtWidgets, QtTest
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

import gui
from backend_layer.facade import Facade
from backend_layer.models.guest import Guest
from gui.games.connect4 import level_of_difficulty
from gui.games.connect4 import GUI, start_game
from gui import tournament_setup, tournament_page
from gui.games.trivia import trivia_gui

mode = 1
difficult = 3
last_game_window = 0


def signup_to_gamespace():
    if signup.Window.sign_up_db():
        open_gamespace()


def signin_to_gamespace():
    if signin.Window.sign_in_db():
        open_gamespace()


def open_startpage():  # home page
    widget.setCurrentIndex(0)
    f = Facade.get_instance()
    if gui.player_global is not None and type(gui.player_global).__name__ != 'Guest':
        f.save_player()
        gui.player_global = Guest()
        f.reset_player()
    w.refresh()


def open_signin():
    widget.setCurrentIndex(1)
    signin.refresh()


def open_signup():
    widget.setCurrentIndex(2)
    signup.refresh()


def open_gamespace():
    widget.setCurrentIndex(3)
    game.refresh()


def open_profile():
    widget.setCurrentIndex(4)
    profile.refresh()


def open_leaderboard():
    widget.setCurrentIndex(5)
    leaderboard.refresh()


def open_tournament_setup():
    widget.setCurrentIndex(10)  # 5
    tournament_setup.refresh()


def open_achievements():
    widget.setCurrentIndex(6)
    achievements_page.refresh()


def open_startgame():
    widget.setCurrentIndex(7)
    startgame.refresh()


def open_levelpage(m):
    widget.setCurrentIndex(8)
    gamelevel.refresh()
    global mode
    mode = m


def open_connect4(k):
    global mode, last_game_window
    last_game_window = 7  # start_game page
    widget.setCurrentIndex(9)
    connect4.K = k
    connect4.mode = mode
    player0 = Guest.build_guest('player')  # dummy player
    player1 = gui.player_global if mode == 0 else Guest.build_guest(gui.player_global.get_name())  # mode
    connect4.set_player(player0, player1)
    connect4.game()


def open_connect4_pp():
    global mode
    mode = 1
    open_connect4(1)


def open_last_game_window():
    print('open_last_game_window : ', last_game_window)
    widget.setCurrentIndex(last_game_window)
    widget.widget(last_game_window).refresh()


def open_tournament():
    if tournament_setup.Window.start_tournament():
        tournament.refresh()
        widget.setCurrentIndex(11)


def open_connect4_tournament():
    global last_game_window
    last_game_window = 11  # tournament page
    widget.setCurrentIndex(9)
    connect4.mode = 1  # 2 players
    f = Facade.get_instance()
    player1, player2 = f.get_current_match()
    connect4.set_player(player1['player'], player2['player'])
    connect4.game()


def open_trivia():
    '''
    global mode, last_game_window
    last_game_window = 7  # start_game page
    widget.setCurrentIndex(9)
    connect4.K = k
    connect4.mode = mode
    player0 = Guest.build_guest('player')  # dummy player
    player1 = gui.player_global if mode == 0 else Guest.build_guest(gui.player_global.get_name())  # mode
    connect4.set_player(player0, player1)
    connect4.game()
    '''
    global last_game_window
    last_game_window = 3  # gamespace page
    start_trivia.refresh()
    start_trivia.set_player(gui.player_global)
    widget.setCurrentIndex(12)


def open_trivia_tournament():
    global last_game_window
    last_game_window = 11  # tournament page
    f = Facade.get_instance()
    player1, player2 = f.get_current_match()
    start_trivia.refresh()
    start_trivia.set_player(player1['player'], player2['player'])
    widget.setCurrentIndex(12)
    trivia_gui.start_game(2)


def open_tournament_game():
    f = Facade.get_instance()
    game_name = f.get_game()
    print(game_name)
    if game_name is not None and game_name == 'connect4':
        print('go to connect 4')
        open_connect4_tournament()
    elif game_name is not None and game_name == 'trivia':
        print('go to trivia')
        open_trivia_tournament()


if __name__ == '__main__':
    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("../storage/Sounds/mixkit-alien-world-trailer-intro-2425.wav")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)
    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.play()
    app = QApplication(sys.argv)
    landing = landing_page.LandingMain()
    # start widget
    widget = QtWidgets.QStackedWidget()
    w = start_page.StartMain()
    signin = signIn.SigninMain()
    signup = signUp.SignupMain()
    game = gamespace.GamespaceMain()
    profile = profile_page.ProfileMain()
    leaderboard = leaderboard.LeaderboardMain()
    tournament_setup = tournament_setup.TournamentSetupMain()
    tournament = tournament_page.TournamentMain()
    achievements_page = achievements_page.AchievementsMain()
    startgame = start_game.StartGameMain()
    gamelevel = level_of_difficulty.StartLevelMain()
    connect4 = GUI.MainWindow()
    start_trivia = trivia_gui.StartGameMain()
    trivia = start_trivia.Window
    # start page
    w.Window.signin_btn.clicked.connect(open_signin)
    w.Window.signup_btn.clicked.connect(open_signup)
    w.Window.guest_btn.clicked.connect(open_gamespace)
    w.Window.quit_btn.clicked.connect(sys.exit)
    # sign in navigation btns
    signin.Window.next_button.clicked.connect(signin_to_gamespace)
    signin.Window.back_button.clicked.connect(open_startpage)
    # sign up navigation btns
    signup.Window.next_button.clicked.connect(signup_to_gamespace)
    signup.Window.back_button.clicked.connect(open_startpage)
    # gamespace navigation btns
    game.Window.profilebtn.clicked.connect(open_profile)
    game.Window.exitbtn.clicked.connect(open_startpage)
    game.Window.leaderboardbtn.clicked.connect(open_leaderboard)
    game.Window.tournamentbtn.clicked.connect(open_tournament_setup)
    game.Window.connect4.clicked.connect(open_startgame)
    game.Window.trivia.clicked.connect(open_trivia)
    # profile navigation btns
    profile.Window.back_button.clicked.connect(open_gamespace)
    profile.Window.achievements_button.clicked.connect(open_achievements)
    # leaderboard navigation
    leaderboard.Window.back_button.clicked.connect(open_gamespace)
    # tournament_setup
    tournament_setup.Window.quit_btn.clicked.connect(open_gamespace)
    tournament_setup.Window.start_tour_btn.clicked.connect(open_tournament)
    # tournament
    tournament.Window.back_button.clicked.connect(open_gamespace)
    tournament.Window.start_button.clicked.connect(open_tournament_game)
    # achievements page
    achievements_page.Window.back_btn.clicked.connect(open_profile)
    # start game
    startgame.Window.pc_btn.clicked.connect(lambda: open_levelpage(0))
    startgame.Window.pp_btn.clicked.connect(open_connect4_pp)
    startgame.Window.quit_btn.clicked.connect(open_gamespace)
    # game level
    gamelevel.Window.easy_btn.clicked.connect(lambda: open_connect4(1))
    gamelevel.Window.normal_btn.clicked.connect(lambda: open_connect4(3))
    gamelevel.Window.hard_btn.clicked.connect(lambda: open_connect4(6))
    gamelevel.Window.quit_btn.clicked.connect(open_startgame)
    # connect4
    connect4.quitbtn.clicked.connect(open_last_game_window)
    # trivia
    start_trivia.quitbtn.clicked.connect(open_last_game_window)

    widget.addWidget(w)  # 0
    widget.addWidget(signin)  # 1
    widget.addWidget(signup)  # 2
    widget.addWidget(game)  # 3
    widget.addWidget(profile)  # 4
    widget.addWidget(leaderboard)  # 5
    widget.addWidget(achievements_page)  # 6
    widget.addWidget(startgame)  # 7
    widget.addWidget(gamelevel)  # 8
    widget.addWidget(connect4)  # 9
    widget.addWidget(tournament_setup)  # 10
    widget.addWidget(tournament)  # 11
    widget.addWidget(trivia)  # 12

    loop = QEventLoop()
    t = QElapsedTimer()
    for i in range(6):
        landing.Window.progressBar.setValue(i * 20)
        QtTest.QTest.qWait(400)

    QTimer.singleShot(500, loop.quit)
    loop.exec_()

    player.stop()
    del landing
    widget.showFullScreen()
    # widget.show()
   # widget.move(10, 10)
    # widget.update()
    sys.exit(app.exec_())
