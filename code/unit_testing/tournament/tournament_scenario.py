import unittest

from backend_layer.models.tournament import Tournament

unittest.TestLoader.sortTestMethodsUsing = None

# test normal sequence of tournament with 4 players and 1 tie (current case in gui)
'''
    0 vs 1          2 vs 3
      |               |
      |             2 vs 3
      |                |
      0                2
      \                /
        \             /
            0 vs 2
              |
           winner : 2
            
0 vs 1  -> 0
2 vs 3  -> tie
2 vs 3  -> 2
0 vs 2  -> 2
winner: 2
'''


class MyTestCase(unittest.TestCase):
    names = ["nada", "mariam", "eman", "manar"]
    tour = Tournament.build_tournament("connect4", names)

    def test_a_get_match_before_next(self):
        self.assertIsNone(self.tour.get_match())

    def test_b_get_match1(self):
        match = self.tour.next_match()
        self.assertIsNotNone(match)
        p1, p2 = match
        self.assertEqual(p1, 0)
        self.assertEqual(p2, 1)

    def test_c_push_winner1(self):
        p2 = self.tour.get_player(1)
        p2['state'] = False  # make p2 lose
        self.assertTrue(self.tour.push_winner(0))
        self.assertTrue(self.tour.get_player(0)['state'])
        self.assertFalse(self.tour.get_player(1)['state'])
        self.assertEqual(self.tour.get_player(0)['wins'], 1)
        self.assertEqual(self.tour.get_player(1)['wins'], 0)

    def test_d_get_match2(self):
        match = self.tour.next_match()
        self.assertIsNotNone(match)
        p1, p2 = match
        self.assertEqual(p1, 2)
        self.assertEqual(p2, 3)

    def test_e_tie(self):
        self.assertTrue(self.tour.push_tie(2, 3))
        self.assertTrue(self.tour.get_player(2)['state'])
        self.assertTrue(self.tour.get_player(3)['state'])
        self.assertEqual(self.tour.get_player(2)['wins'], 0)
        self.assertEqual(self.tour.get_player(3)['wins'], 0)

    def test_f_get_match3(self):
        match = self.tour.next_match()
        self.assertIsNotNone(match)
        p1, p2 = match
        self.assertEqual(p1, 2)
        self.assertEqual(p2, 3)

    def test_g_push_winner2(self):
        p2 = self.tour.get_player(3)
        p2['state'] = False  # make p2 lose
        self.assertTrue(self.tour.push_winner(2))
        self.assertTrue(self.tour.get_player(2)['state'])
        self.assertFalse(self.tour.get_player(3)['state'])
        self.assertEqual(self.tour.get_player(2)['wins'], 1)
        self.assertEqual(self.tour.get_player(3)['wins'], 0)

    def test_h_get_match4(self):
        match = self.tour.next_match()
        self.assertIsNotNone(match)
        p1, p2 = match
        self.assertEqual(p1, 0)
        self.assertEqual(p2, 2)

    def test_i_push_winner2(self):
        p2 = self.tour.get_player(0)
        p2['state'] = False  # make p2 lose
        self.assertTrue(self.tour.push_winner(2))
        self.assertTrue(self.tour.get_player(2)['state'])
        self.assertFalse(self.tour.get_player(0)['state'])
        self.assertEqual(self.tour.get_player(2)['wins'], 2)
        self.assertEqual(self.tour.get_player(0)['wins'], 1)

    def test_j_end_tour(self):
        match = self.tour.next_match()
        self.assertIsNone(match)

    def test_k_check_winner(self):
        winner = self.tour.get_winner()
        self.assertIsNotNone(winner)
        self.assertEqual(winner['id'], 2)
        self.assertEqual(winner['wins'], 2)
        self.assertTrue(winner['state'])


if __name__ == '__main__':
    unittest.main()
