import os

from backend_layer.auth_proxy.hashing import hash_password
from backend_layer.database.db_manager import DBManager


class Updater:
    __instance = None

    def __init__(self):
        self.__secret_token = "6390ed339b8270b"
        if Updater.__instance is not None:
            raise Exception("Can't create another instance of Updater")
        else:  # first instance
            Updater.__instance = self  # static private variable
            self.__db = DBManager.get_instance(self.__secret_token)

    @staticmethod
    def get_instance():
        if Updater.__instance is not None:
            return Updater.__instance
        else:
            Updater.__instance = Updater()
            return Updater.__instance

    @staticmethod
    def reset_instance():
        Updater.__instance = None

    def save_player(self, player):
        return self.__db.update_player(player)

    def save_name(self, player, new_name):
        if self.__db.update_name(player.get_name(), new_name):
            print('here')
            # reset avatar picture file name
            old_avatar = player.get_avatar()
            new_avatar = old_avatar.replace(player.get_name(), new_name)
            player.set_name(new_name)
            player.set_avatar(new_avatar)
            os.rename(old_avatar, new_avatar)
            return True
        else:
            return False

    def save_password(self, player, old_password, new_password):
        password, salt = self.__db.get_password(player.get_name())
        if len(password) == 0 or len(salt) == 0:
            return False, None
        if password != hash_password(bytes.fromhex(salt), old_password).hex():
            return False, "Wrong password"  # wrong password
        if len(new_password) < 8:
            return False, "Invalid password"
        return self.__db.update_password(player.get_name(), password, hash_password(bytes.fromhex(salt), new_password).hex()), None

