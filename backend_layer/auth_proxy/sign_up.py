import abc

from backend_layer.auth_proxy.hashing import generate_salt, hash_password
from backend_layer.database.db_manager import DBManager


# formal interface


class SignUpInterface(abc.ABC):
    def sign_up(self, name, password, gender):
        pass


# class implements the interface
class SignUp(SignUpInterface):

    def __init__(self):
        self.__secret_token = "6390ed339b8270b"
        try:
            self.db = DBManager.get_instance(self.__secret_token)
        except Exception as e:
            print(e)

    def sign_up(self, name, password, gender):
        """
        Create new player
        :param name
        :param password
        :param gender
        :return: true and player object or false and an error message
        """
        print("in proxy")
        if not SignUp.__validate_password(password):
            return False, "Invalid password!"
        elif self.db.check_name(name):
            return False, "Name already exists!"
        else:
            salt = generate_salt()
            password = hash_password(salt, password)
            return self.db.add_player(name, password.hex(), salt.hex(), gender)

    # check password
    @staticmethod
    def __validate_password(password):
        return len(password) >= 8