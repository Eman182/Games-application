import unittest

from backend_layer.database.db_manager import DBManager
from backend_layer.models.player import Player
from backend_layer.models.xp_achievement import XpAchievement

correct_token = "6390ed339b8270b"
wrong_token = "1390ed339b8270b"
salt = "32abcdef"
p = "password1234"


class MyTestCase(unittest.TestCase):

    def test_connection_failure_default_quote(self):
        db = DBManager.get_instance(correct_token)
        db.close()
        # connection failure, each method returns a default value
        self.assertEqual(db.get_quote(), "Welcome Alien")  # default
        self.assertFalse(db.add_quote("dummy"))  # false

        db.reset_instance()

    def test_connection_failure_default_player(self):
        db = DBManager.get_instance(correct_token)
        db.close()
        # connection failure, each method returns a default value
        self.assertFalse(db.check_name("dummy"))  # false
        self.assertEqual(db.get_password("dummy"), ("", ""))
        self.assertEqual(db.get_player("dummy"), (False, None))
        self.assertEqual(db.add_player("dummy", "password", "salt"), (False, None))
        self.assertFalse(db.update_player(Player()))
        self.assertFalse(db.update_name("old dummy", "new dummy"))
        self.assertFalse(db.update_password("dummy", "password1", "password2"))

        db.reset_instance()

    def test_connection_failure_default_achievements(self):
        db = DBManager.get_instance(correct_token)
        db.close()
        # connection failure, each method returns a default value
        self.assertFalse(db.create_achievements("dummy"))
        self.assertEqual(db.get_achievements("dummy"), [])
        self.assertFalse(db.update_db_achievements([XpAchievement(10,"dummy", 0, 1)], "dummy"))

        db.reset_instance()

    def test_connection_failure_default_leaderboard(self):
        db = DBManager.get_instance(correct_token)
        db.close()
        # connection failure, each method returns a default value
        self.assertEqual(db.get_leaderboard(), [])

        db.reset_instance()

    def test_get_quote(self):
        db = DBManager.get_instance(correct_token)
        self.assertNotEqual(db.get_quote(), "Welcome Alien")  # successful query, don't get default

        DBManager.reset_instance()

    def test_add_quote(self):
        db = DBManager.get_instance(correct_token)
        # valid input
        self.assertTrue(db.add_quote("Never give up"))  # successful addition
        # invalid inputs
        self.assertFalse(db.add_quote(None))
        self.assertFalse(db.add_quote(""))
        self.assertFalse(db.add_quote(85))

        DBManager.reset_instance()

    def test_check_name(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.check_name(""))
        self.assertFalse(db.check_name(None))
        self.assertFalse(db.check_name(20))
        # user doesn't exist
        self.assertFalse(db.check_name("non-existing player"))
        # user exists
        db.add_player("Game1", p, salt)
        self.assertTrue(db.check_name("Game1"))  # user exists

        DBManager.reset_instance()

    def test_get_password(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertEqual(db.get_password(""), ("", ""))
        self.assertEqual(db.get_password(None), ("", ""))
        self.assertEqual(db.get_password(20), ("", ""))
        # user doesn't exist
        self.assertEqual(db.get_password("non-existing player"), ("", ""))
        # user exists
        db.add_player("Game2", p, salt)
        self.assertEqual(db.get_password("Game2"), (p, salt))  # user exists

        DBManager.reset_instance()

    def test_get_player(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertEqual(db.get_player(""), (False, None))
        self.assertEqual(db.get_player(None), (False, None))
        self.assertEqual(db.get_player(20), (False, None))
        # user doesn't exist
        self.assertEqual(db.get_player("non-existing player"), (False, None))
        # user exists
        db.add_player("Game3", p, salt)
        check, player = db.get_player("Game3")
        self.assertTrue(check)  # user exists
        self.assertIsNotNone(player)

        DBManager.reset_instance()

    def test_add_player(self):
        db = DBManager.get_instance(correct_token)
        # invalid inputs
        self.assertEqual(db.add_player("", "", None, 0), (False, None))
        self.assertEqual(db.add_player(None, 0, ""), (False, None))
        self.assertEqual(db.add_player("", "", "", ""), (False, None))

        # add new player
        check, player = db.add_player("Game", p, salt)
        self.assertTrue(check)
        self.assertIsNotNone(player)
        self.assertEqual(player.get_name(), "Game")
        self.assertFalse(player.get_gender())  # default gender false
        self.assertEqual(db.get_password("Game"), (p, salt))

        # add existing player
        self.assertEqual(db.add_player("Game", p, salt), (False, None))

        DBManager.reset_instance()

    def test_update_player_invalid(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_player(None))
        self.assertFalse(db.update_player(25))
        self.assertFalse(db.update_player("player"))
        # player doesn't exist
        player = Player.build_player("non-existing player")
        self.assertFalse(db.update_player(player))

        DBManager.reset_instance()

    def test_update_player_exist(self):
        db = DBManager.get_instance(correct_token)
        # player exists
        db.add_player("Game4", p, salt)
        check, player = db.get_player("Game4")
        player.set_games(10)
        player.increase_weekly_xp(100)
        self.assertTrue(db.update_player(player))
        # check the returned Game4
        check, returned = db.get_player("Game4")
        self.assertTrue(check)
        self.assertEqual(returned.get_name(), player.get_name())
        self.assertEqual(returned.get_avatar(), player.get_avatar())
        self.assertEqual(returned.get_level(), player.get_level())
        self.assertEqual(returned.get_xp(), player.get_xp())
        self.assertEqual(returned.get_weekly_xp(), player.get_weekly_xp())
        self.assertEqual(returned.get_wins(), player.get_wins())
        self.assertEqual(returned.get_games(), player.get_games())
        self.assertEqual(returned.get_daily_challenges(), player.get_daily_challenges())
        self.assertEqual(returned.get_games(), player.get_games())

        DBManager.reset_instance()

    def test_update_name(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_name(0, 5))
        self.assertFalse(db.update_name("", None))

        # player doesn't exist
        self.assertFalse(db.update_name("non-existing player", "new_player"))

        # player exists
        db.add_player("Game5", p, salt)
        self.assertTrue(db.update_name("Game5", "Game55"))
        self.assertTrue(db.check_name("Game55"))
        self.assertFalse(db.check_name("Game5"))

        DBManager.reset_instance()

    def test_update_password(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_password(0, 5, 6))
        self.assertFalse(db.update_password("", None, None))
        # player doesn't exist
        self.assertFalse(db.update_password("non-existing player", "new password", "514"))
        # player exists
        db.add_player("Game6", p, salt)
        self.assertTrue(db.update_password("Game6", p, "new password"))
        self.assertEqual(db.get_password("Game6"), ("new password", salt))
        self.assertNotEqual(db.get_password("Game6"), (p, salt))

        DBManager.reset_instance()

    def test_create_achievements(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.create_achievements(""))
        self.assertFalse(db.create_achievements(None))
        self.assertFalse(db.create_achievements(20))
        # player doesn't exist
        self.assertFalse(db.create_achievements("non-existing player"))

        DBManager.reset_instance()

    def test_get_achievements(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.get_achievements(""))
        self.assertFalse(db.get_achievements(None))
        self.assertFalse(db.get_achievements(20))
        # player doesn't exist
        self.assertEqual(db.get_achievements("non-existing player"), [])

        DBManager.reset_instance()

    def test_update_db_achievements(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_db_achievements("", ""))
        self.assertFalse(db.update_db_achievements(None, None))
        self.assertFalse(db.update_db_achievements(20, 20))
        # player doesn't exist
        self.assertFalse(db.update_db_achievements([XpAchievement(10, "dummy", 0, 1)], "non-existing player"))
        self.assertFalse(db.update_db_achievements([], "non-existing player"))

        DBManager.reset_instance()


if __name__ == '__main__':
    unittest.main()
