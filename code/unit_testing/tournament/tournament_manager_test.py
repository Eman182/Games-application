import unittest

from backend_layer.access_managers.tournament_manager import TournamentManager


class MyTestCase(unittest.TestCase):
    names = ['manar', 'nour', 'eman', 'nada']
    tour_mgr = TournamentManager.get_instance()

    def test_a_build_tour(self):
        self.assertFalse(self.tour_mgr.tour_exist())
        self.assertTrue(self.tour_mgr.build_tournament("trivia", self.names))
        self.assertTrue(self.tour_mgr.tour_exist())

    def test_b_get_game(self):
        self.assertEqual("trivia", self.tour_mgr.get_game())

    def test_c_next_match(self):
        self.assertIsNone(self.tour_mgr.get_current_match())
        match = self.tour_mgr.next_match()
        self.assertIsNotNone(match)
        self.assertEqual(match, self.tour_mgr.get_current_match())
        p1, p2 = match  # player_obj
        self.assertEqual("manar", p1['player'].get_name())
        self.assertEqual(p1['id'],0)
        self.assertEqual("nour", p2['player'].get_name())
        self.assertEqual(p2['id'],1)

    def test_d_winner1(self):
        match1 = self.tour_mgr.get_current_match()
        p1, p2= match1
        p1['player'].report_game(True,10)
        p2['player'].report_game(False,5)
        match2 = self.tour_mgr.next_match()
        self.assertIsNotNone(match2)
        self.assertNotEqual(match2,match1)
        self.assertEqual(p1['player'].get_xp(),0)
        self.assertEqual(p2['player'].get_xp(),0)
        self.assertEqual(p1['wins'],1)
        self.assertEqual(p2['wins'],0)
        self.assertTrue(p1['state'])
        self.assertFalse(p2['state'])

    def test_e_match2(self):
        self.assertIsNotNone(self.tour_mgr.get_current_match())
        match = self.tour_mgr.get_current_match()
        p1, p2 = match  # player_obj
        self.assertEqual("eman", p1['player'].get_name())
        self.assertEqual(p1['id'],2)
        self.assertEqual("nada", p2['player'].get_name())
        self.assertEqual(p2['id'],3)

    def test_f_winner2(self):
        match1 = self.tour_mgr.get_current_match()
        p1, p2 = match1
        p1['player'].report_game(False, 10)
        p2['player'].report_game(True, 15)
        match2 = self.tour_mgr.next_match()
        self.assertIsNotNone(match2)
        self.assertNotEqual(match2, match1)
        self.assertEqual(p1['player'].get_xp(), 0)
        self.assertEqual(p2['player'].get_xp(), 0)
        self.assertEqual(p1['wins'], 0)
        self.assertEqual(p2['wins'], 1)
        self.assertFalse(p1['state'])
        self.assertTrue(p2['state'])

    def test_g_get_winner(self):
        self.assertIsNone(self.tour_mgr.get_winner())

    def test_h_match3(self):
        self.assertIsNotNone(self.tour_mgr.get_current_match())
        match = self.tour_mgr.get_current_match()
        p1, p2 = match  # player_obj
        self.assertEqual("manar", p1['player'].get_name())
        self.assertEqual(p1['id'],0)
        self.assertEqual("nada", p2['player'].get_name())
        self.assertEqual(p2['id'],3)

    def test_i_winner3(self):
        match1 = self.tour_mgr.get_current_match()
        p1, p2 = match1
        p1['player'].report_game(False, 10)
        p2['player'].report_game(True, 15)
        match2 = self.tour_mgr.next_match()
        self.assertIsNone(match2) # final match
        self.assertNotEqual(match2, match1)
        self.assertEqual(p1['player'].get_xp(), 0)
        self.assertEqual(p2['player'].get_xp(), 0)
        self.assertEqual(p1['wins'], 1)
        self.assertEqual(p2['wins'], 2)
        self.assertFalse(p1['state'])
        self.assertTrue(p2['state'])

    def test_j_next_match_after_finish(self):
        self.assertIsNone(self.tour_mgr.get_current_match())
        self.assertIsNone(self.tour_mgr.next_match())

    def test_k_get_winner(self):
        winner = self.tour_mgr.get_winner()
        self.assertEqual('nada', winner['player'].get_name())
        self.assertEqual(winner['wins'], 2)
        self.assertEqual(winner['id'], 3)
        self.assertTrue(winner['state'])
        self.assertEqual(winner['player'].get_xp(), 0)


if __name__ == '__main__':
    unittest.main()
