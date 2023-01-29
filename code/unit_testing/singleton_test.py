import unittest

from backend_layer.access_managers.tournament_manager import TournamentManager
from backend_layer.facade import Facade
from backend_layer.access_managers.getter import Getter
from backend_layer.access_managers.updater import Updater
from backend_layer.database.db_manager import DBManager

correct_token = "6390ed339b8270b"
wrong_token = "1390ed339b8270b"
salt = "32abcdef"

# TestLoader.sortTestMethodsUsing = lambda self, a, b: (a > b) - (a < b)


class MyTestCase(unittest.TestCase):

    def test11_db_wrong_token(self):  # first connection with init
        with self.assertRaises(Exception):  # wrong token first initialization
            db = DBManager(wrong_token)

        with self.assertRaises(Exception):  # wrong token with get instance
            db = DBManager.get_instance(wrong_token)

        DBManager.reset_instance()  # reset instance

    def test12_db_second_init(self):
        db = DBManager(correct_token)  # correct and first

        with self.assertRaises(Exception):  # correct token second initialization
            db = DBManager(correct_token)

        DBManager.reset_instance()  # reset instance

    def test13_db_same_instance(self):
        db1 = DBManager.get_instance(correct_token)
        db2 = DBManager.get_instance(correct_token)
        self.assertEqual(db1, db2)  # same instance

        DBManager.reset_instance()  # reset instance

    def test21_updater_second_init(self):
        u = Updater()  # first
        with self.assertRaises(Exception):  # second initialization
            u = Updater()

        Updater.reset_instance()  # reset instance

    def test22_updater_same_instance(self):
        u1 = Updater.get_instance()
        u2 = Updater.get_instance()
        self.assertEqual(u1, u2)  # same instance

        Updater.reset_instance()  # reset instance

    def test23_updater_same_instance2(self):
        u1 = Updater()
        u2 = Updater.get_instance()
        self.assertEqual(u1, u2)  # same instance

        Updater.reset_instance()  # reset instance

    def test24_updater_init_after_get_instance(self):
        u1 = Updater.get_instance()
        with self.assertRaises(Exception):  # correct token second initialization
            u2 = Updater()
        u2 = Updater.get_instance()
        self.assertEqual(u1, u2)

        Updater.reset_instance()
        
    def test31_getter_second_init(self):
        g = Getter()  # first
        with self.assertRaises(Exception):  # second initialization
            g = Getter()

        Getter.reset_instance()  # reset instance

    def test32_getter_same_instance(self):
        g1 = Getter.get_instance()
        g2 = Getter.get_instance()
        self.assertEqual(g1, g2)  # same instance

        Getter.reset_instance()  # reset instance

    def test33_getter_same_instance2(self):
        g1 = Getter()
        g2 = Getter.get_instance()
        self.assertEqual(g1, g2)  # same instance

        Getter.reset_instance()  # reset instance

    def test34_getter_init_after_get_instance(self):
        g1 = Getter.get_instance()
        with self.assertRaises(Exception):  # correct token second initialization
            g2 = Getter()
        g2 = Getter.get_instance()
        self.assertEqual(g1, g2)

        Getter.reset_instance()

    def test41_tournament_manager_second_init(self):
        t = TournamentManager()  # first
        with self.assertRaises(Exception):  # second initialization
            t = TournamentManager()

        TournamentManager.reset_instance()  # reset instance

    def test42_tournament_manager_same_instance(self):
        t1 = TournamentManager.get_instance()
        t2 = TournamentManager.get_instance()
        self.assertEqual(t1, t2)  # same instance

        TournamentManager.reset_instance()  # reset instance

    def test43_tournament_manager_same_instance2(self):
        t1 = TournamentManager()
        t2 = TournamentManager.get_instance()
        self.assertEqual(t1, t2)  # same instance

        TournamentManager.reset_instance()  # reset instance

    def test44_tournament_manger_init_after_get_instance(self):
        t1 = TournamentManager.get_instance()
        with self.assertRaises(Exception):  # correct token second initialization
            t2 = TournamentManager()
        t2 = TournamentManager.get_instance()
        self.assertEqual(t1, t2)

        TournamentManager.reset_instance()

    def test51_facade_second_init(self):
        f = Facade()  # first
        with self.assertRaises(Exception):  # second initialization
            f = Facade()

        Facade.reset_instance()  # reset instance

    def test52_facade_same_instance(self):
        f1 = Facade.get_instance()
        f2 = Facade.get_instance()
        self.assertEqual(f1, f2)  # same instance

        Facade.reset_instance()  # reset instance

    def test53_facade_same_instance2(self):
        f1 = Facade()
        f2 = Facade.get_instance()
        self.assertEqual(f1, f2)  # same instance

        Facade.reset_instance()  # reset instance

    def test54_facade_init_after_get_instance(self):
        f1 = Facade.get_instance()
        with self.assertRaises(Exception):  # correct token second initialization
            f2 = Facade()
        f2 = Facade.get_instance()
        self.assertEqual(f1, f2)

        Facade.reset_instance()


if __name__ == '__main__':
    unittest.main()
