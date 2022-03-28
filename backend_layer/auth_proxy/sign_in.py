import abc

from backend_layer.auth_proxy.hashing import hash_password
from backend_layer.database.db_manager import DBManager


class SignInInterface(abc.ABC):
    def sign_in(self, username, password):
        pass


class SignIn(SignInInterface):

    def __init__(self):
        self.__secret_token = "6390ed339b8270b"
        try:
            self.db = DBManager.get_instance(self.__secret_token)
        except Exception as e:
            print(e)

    def sign_in(self, user_name, password):
        """
        Authenticate users
        :param user_name
        :param password
        :return: true and player if player has logged in successfully or false and message error otherwise
        """
        original_pw, salt = self.db.get_password(user_name)
        if len(salt) < 64:
            return False, "Player doesn't exist!"
        else:
            hashed_password = hash_password(bytes.fromhex(salt), password)
            if hashed_password.hex() != original_pw:
                return False, "Wrong password!"
            else:
                return self.db.get_player(user_name)  # may return null