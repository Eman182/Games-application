import unittest
from backend_layer.models.tournament import Tournament


class MyTestCase(unittest.TestCase):
    def test_build_wrong_game(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('8-puzzles', pnames)
        self.assertIsNone(tour)

    def test_build_wrong_game_format(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect 4', pnames)
        self.assertIsNone(tour)

    def test_build_valid_input(self):
        pnames = ['eman', 'manar', 'nour']
        # connect4
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('  connect4', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('connect4  ', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('  connect4  ', pnames)
        self.assertIsNotNone(tour)

        # trivia
        tour = Tournament.build_tournament('trivia', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('  trivia', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('trivia  ', pnames)
        self.assertIsNotNone(tour)
        tour = Tournament.build_tournament('  trivia  ', pnames)
        self.assertIsNotNone(tour)

    def test_build_wrong_names_none_list(self):
        pnames = None
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour)

    def test_build_wrong_names_empty_str(self):
        pnames = ['', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour)

    def test_build_wrong_names_none_str(self):
        pnames = [None, None, None]
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour)

    def test_build_wrong_names_type(self):
        pnames = [1, 2, 4]
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour)

    def test_build_invalid_names_len(self):
        pnames = ['nada', 'mariam']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour)

    def test_get_player_invalid_id_type(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour.get_player(-1))

    def test_get_player_empty_id(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour.get_player())

    def test_get_player_wrong_id_type(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour.get_player("0"))

    def test_get_player_none_id(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour.get_player(None))

    def test_get_player_id_out_bounds(self):
        pnames = ['eman', 'manar', 'nour']
        tour = Tournament.build_tournament('connect4', pnames)
        self.assertIsNone(tour.get_player(4))

    def test_get_player_id_valid(self):
        pnames = ['eman', 'manar', 'nour', 'nada', 'mariam']
        tour = Tournament.build_tournament('connect4', pnames)
        tour_player = tour.get_player(1)
        self.assertEqual(tour_player['player'].get_name(), "manar")
        self.assertTrue(tour_player['state'])
        self.assertEqual(tour_player['wins'], 0)
        self.assertEqual(tour_player['color'], "red")
        self.assertEqual(tour_player['id'], 1)

    def test_get_game_wrong_name(self):
        tour = Tournament()
        tour.set_game('connect 4')
        self.assertIsNone(tour.get_game())

    def test_get_game_none(self):
        tour = Tournament()
        tour.set_game(None)
        self.assertIsNone(tour.get_game())

    def test_get_game_wrong_type(self):
        tour = Tournament()
        tour.set_game(55)
        self.assertIsNone(tour.get_game())

    def test_get_game_empty_str(self):
        tour = Tournament()
        tour.set_game('')
        self.assertIsNone(tour.get_game())

    def test_get_game_valid(self):
        tour = Tournament()
        tour.set_game('connect4')
        self.assertEqual('connect4', tour.get_game())

        tour = Tournament()
        tour.set_game('coNNect4')
        self.assertEqual('connect4', tour.get_game())

        tour = Tournament()
        tour.set_game('TRIVIA')
        self.assertEqual('trivia', tour.get_game())

        tour = Tournament()
        tour.set_game('  connect4  ')
        self.assertEqual('connect4', tour.get_game())

    def test_get_players_wrong_len(self):
        tour = Tournament()
        tour.set_players(["nada", "mariam"])
        self.assertIsNone(tour.get_players())

    def test_get_players_none(self):
        tour = Tournament()
        tour.set_players(None)
        self.assertIsNone(tour.get_players())

    def test_get_players_wrong_type(self):
        tour = Tournament()
        tour.set_players(20)
        self.assertIsNone(tour.get_players())

    def test_get_players_empty_str(self):
        tour = Tournament()
        tour.set_players(["", "", "", ""])
        self.assertIsNone(tour.get_players())

    def test_get_players_valid(self):
        tour = Tournament()
        tour.set_players(["nada", "nada", "manar"])
        self.assertIsNotNone(tour.get_players())
        self.assertEqual(len(tour.get_players()), 3)


if __name__ == '__main__':
    unittest.main()
