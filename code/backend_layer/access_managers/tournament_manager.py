from backend_layer.models.tournament import Tournament


class TournamentManager:
    __instance = None

    def __init__(self):
        self.__secret_token = "6390ed339b8270b"
        if TournamentManager.__instance is not None:
            raise Exception("Can't create another instance of TournamentManager")
        else:  # first instance
            TournamentManager.__instance = self  # static private variable
            self.tournament = None

    @staticmethod
    def get_instance():
        if TournamentManager.__instance is not None:
            return TournamentManager.__instance
        else:
            TournamentManager.__instance = TournamentManager()
            return TournamentManager.__instance

    @staticmethod
    def reset_instance():
        TournamentManager.__instance = None

    def build_tournament(self, game, names):
        tournament = Tournament.build_tournament(game, names)
        if tournament is not None:
            self.tournament = tournament
            return True
        return False

    def close_tournament(self):
        self.tournament = None

    def tour_exist(self):
        return self.tournament is not None

    def get_tournament_players(self):
        return self.tournament.get_players() if self.tour_exist() else None

    def get_game(self):
        return self.tournament.get_game() if self.tour_exist() else None

    def get_winner(self):
        return self.tournament.get_winner() if self.tour_exist() else None

    def next_match(self):
        self.update_state()
        if self.tour_exist():
            match = self.tournament.next_match()
            if match is not None:
                p1, p2 = match
                return self.tournament.get_player(p1), self.tournament.get_player(p2)

        return None

    def get_current_match(self):
        if self.tour_exist():
            match = self.tournament.get_match()
            if match is not None:
                p1, p2 = match
                return self.tournament.get_player(p1), self.tournament.get_player(p2)
        return None

    def update_state(self):
        if self.tour_exist():
            current_match = self.tournament.get_match()  # indices
            if current_match is not None:
                p1, p2 = current_match
                player1_obj, player2_obj = self.tournament.get_player(p1), self.tournament.get_player(p2)
                player1, player2 = player1_obj['player'], player2_obj['player']

                if player1.get_level() > player2.get_level() \
                        or (player1.get_level() == player2.get_level() and player1.get_xp() > player2.get_xp()):
                    self.tournament.push_winner(p1)
                    player2_obj['state'] = False
                elif player2.get_level() > player1.get_level() \
                        or (player2.get_level() == player1.get_level() and player2.get_xp() > player1.get_xp()):
                    self.tournament.push_winner(p2)
                    player1_obj['state'] = False
                else:
                    self.tournament.push_tie(p1, p2)

                player1.reset()
                player2.reset()
                return True
        return False
