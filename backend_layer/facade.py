import os
import shutil

from backend_layer.auth_proxy.sign_in import SignIn
from backend_layer.auth_proxy.sign_up import SignUp
from backend_layer.access_managers.getter import Getter
from backend_layer.models.guest import Guest
from backend_layer.access_managers.tournament_manager import TournamentManager
from backend_layer.access_managers.updater import Updater


class Facade:
    __instance = None

    def __init__(self):
        if Facade.__instance is not None:
            raise Exception("Can't create another instance of Facade")
        else:
            self.player = Guest()
            self.signup = SignUp()
            self.signin = SignIn()
            self.updater = Updater.get_instance()
            self.getter = Getter.get_instance()
            self.tournament_manager = TournamentManager.get_instance()
            Facade.__instance = self

    @staticmethod
    def get_instance():
        if Facade.__instance is not None:
            return Facade.__instance
        else:
            Facade.__instance = Facade()
            return Facade.__instance

    @staticmethod
    def reset_instance():
        Facade.__instance = None

    def signup_request(self, name, password, gender):
        check, player = self.signup.sign_up(name, password, gender)
        if check:
            self.player = player
        return check, player

    def signin_request(self, name, password):
        check, player = self.signin.sign_in(name, password)
        if check:
            self.player = player
        return check, player

    def save_player(self):
        check = self.updater.save_player(self.player)
        if check:
            self.reset_player()
        return check

    def save_name(self, new_name):
        return self.updater.save_name(self.player, new_name)

    def save_password(self, old_password, new_password):
        return self.updater.save_password(self.player, old_password, new_password)

    def change_profile_pic(self, path):
        # path validation
        if not os.path.isfile(path) or not (os.path.splitext(path)[-1] == '.png' or os.path.splitext(path)[-1] == '.jpg' or os.path.splitext(path)[-1] == '.jpeg'):
            return False, None

        try:
            new_path = "..\\storage\\Avatars\\" + self.player.get_name() + os.path.splitext(path)[-1]
            shutil.copyfile(path, new_path)
            self.player.set_avatar(new_path)
            return True, new_path
        except Exception as e:
            print(e)
            return False, None

    def notify_achievements(self, player, achievement_type):
        return self.player.update_achievements(achievement_type)

    def get_achievements(self):
        ach_list = self.player.get_achievements()
        res = []
        for ach in ach_list:
            t = ach.get_description(), ach.get_reward(), ach.get_checked()
            res.append(t)
        return res

    def get_quote(self):
        return self.getter.get_quote()

    def get_leaderboard(self):
        return self.getter.get_leaderboard()

    def reset_player(self):
        self.player = Guest()

    def create_tournament(self, game, names):
        return self.tournament_manager.build_tournament(game, names)

    def get_tournament_players(self):
        return self.tournament_manager.get_tournament_players()

    def get_game(self):
        return self.tournament_manager.get_game()

    def get_next_match(self):
        return self.tournament_manager.next_match()

    def get_current_match(self):
        return self.tournament_manager.get_current_match()

    def get_winner(self):
        return self.tournament_manager.get_winner()
