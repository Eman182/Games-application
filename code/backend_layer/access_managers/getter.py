from backend_layer.database.db_manager import DBManager


class Getter:
    __instance = None

    def __init__(self):
        self.__secret_token = "6390ed339b8270b"
        if Getter.__instance is not None:
            raise Exception("Can't create another instance of Getter")
        else:  # first instance
            Getter.__instance = self  # static private variable
            self.__db = DBManager.get_instance(self.__secret_token)

    @staticmethod
    def get_instance():
        if Getter.__instance is not None:
            return Getter.__instance
        else:
            Getter.__instance = Getter()
            return Getter.__instance

    @staticmethod
    def reset_instance():
        Getter.__instance = None

    def get_quote(self):
        return self.__db.get_quote()

    def get_leaderboard(self):
        return self.__db.get_leaderboard()
