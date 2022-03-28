import unittest
from backend_layer.models.player import Player
from backend_layer.models.wins_achievement import WinsAchievement


class MyTestCase(unittest.TestCase):

    def test_default(self):
        player = Player()
        self.assertEqual(player.get_name(), "Guest")
        self.assertFalse(player.get_gender())
        self.assertEqual(player.get_avatar(), "..\\storage\\icons\\default.jpg")
        self.assertEqual(player.get_level(), 1)
        self.assertEqual(player.get_xp(), 0)
        self.assertEqual(player.get_weekly_xp(), 0)
        self.assertEqual(player.get_wins(), 0)
        self.assertEqual(player.get_games(), 0)
        self.assertEqual(player.get_daily_challenges(), 0)
        self.assertEqual(player.get_achievements(), [])

    def test_build_invalid_input(self):
        player = Player.build_player(None)
        self.assertIsNone(player)

        player = Player.build_player(None, None, None, None, None, None, None, None, None, None)
        self.assertIsNone(player)

        player = Player.build_player("", "", "", "", "", "", "", "", "", "")
        self.assertIsNone(player)

    def test_build_default(self):
        player = Player.build_player("player 1")
        self.assertIsNotNone(player)
        self.assertEqual(player.get_name(), "player 1")
        self.assertFalse(player.get_gender())
        self.assertEqual(player.get_avatar(), "..\\storage\\icons\\default.jpg")
        self.assertEqual(player.get_level(), 1)
        self.assertEqual(player.get_xp(), 0)
        self.assertEqual(player.get_weekly_xp(), 0)
        self.assertEqual(player.get_wins(), 0)
        self.assertEqual(player.get_games(), 0)
        self.assertEqual(player.get_daily_challenges(), 0)
        self.assertEqual(player.get_achievements(), [])

    def test_build(self):
        player = Player.build_player("player 1", True, "path\\file.png", 1, 40, 10, 20, 30, 40, [WinsAchievement(10, "dummy", 0, 1)])
        self.assertIsNotNone(player)
        self.assertEqual(player.get_name(), "player 1")
        self.assertTrue(player.get_gender())
        self.assertEqual(player.get_avatar(), "path\\file.png")
        self.assertEqual(player.get_level(), 1)
        self.assertEqual(player.get_xp(), 40)
        self.assertEqual(player.get_weekly_xp(), 10)
        self.assertEqual(player.get_wins(), 20)
        self.assertEqual(player.get_games(), 30)
        self.assertEqual(player.get_daily_challenges(), 40)
        self.assertEqual(player.get_achievements(), [WinsAchievement(10, "dummy", 0, 1)])

    def test_increase_weekly_xp(self):
        player = Player.build_player("player 2")
        self.assertEqual(player.get_weekly_xp(), 0)
        player.increase_weekly_xp(179)
        self.assertEqual(player.get_weekly_xp(), 179)
        player.increase_weekly_xp(-80)
        self.assertEqual(player.get_weekly_xp(), 179)

    def test_increase_xp(self):
        player = Player.build_player("player 3")
        self.assertEqual(player.get_xp(), 0)
        self.assertEqual(player.get_level(), 1)
        self.assertEqual(player.xp_to_complete(), 50)
        player.increase_xp(40)
        self.assertEqual(player.get_xp(), 40)
        self.assertEqual(player.get_level(), 1)
        self.assertEqual(player.xp_to_complete(), 10)
        player.increase_xp(100)
        self.assertEqual(player.get_xp(), 90)
        self.assertEqual(player.get_level(), 2)
        self.assertEqual(player.xp_to_complete(), 60)
        player.increase_xp(500)
        self.assertEqual(player.get_xp(), 140)
        self.assertEqual(player.get_level(), 4)
        self.assertEqual(player.xp_to_complete(), 360)
        player.increase_xp(360)
        self.assertEqual(player.get_xp(), 0)
        self.assertEqual(player.get_level(), 5)
        self.assertEqual(player.xp_to_complete(), 750)
        player.increase_xp(-360)
        self.assertEqual(player.get_xp(), 0)
        self.assertEqual(player.get_level(), 5)
        self.assertEqual(player.xp_to_complete(), 750)

    def test_increment_wins(self):
        player = Player.build_player("player 2")
        self.assertEqual(player.get_wins(), 0)
        player.increment_wins()
        self.assertEqual(player.get_wins(), 1)

    def test_increment_games(self):
        player = Player.build_player("player 2")
        self.assertEqual(player.get_games(), 0)
        player.increment_games()
        self.assertEqual(player.get_games(), 1)


if __name__ == '__main__':
    unittest.main()
