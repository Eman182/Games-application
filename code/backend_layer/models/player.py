# player model
from backend_layer.models import guest


class Player(guest.Guest):
    """
    A class to represent a player.
    ...
    Attributes
    ----------
    _gender : bool
        False if Male, True if Female
    _weekly_xp : int
        total xp collected by a player during the current week
    _wins : int
        total number of wins in any games played by the player since it was registered
    _games : int
        total number of games played by the player since it was registered
    _daily_challenges : int
        total number of daily challenges completed in a row without missing a single challenge
    Methods
    -------
    set_name(name):
        Returns True if name is valid, False otherwise
    set_avatar(avatar):
        Returns True if avatar path is valid, False otherwise
    set_gender(gender):
        Returns True if gender is valid, False otherwise
    get_gender():
        Returns "Female" or "Male"
    """

    def __init__(self):
        super().__init__()
        self._gender = False
        self._weekly_xp = 0
        self._wins = 0
        self._games = 0
        self._daily_challenges = 0
        self.achievements = []

    @staticmethod
    def build_player(name, gender=False, avatar=None, lvl=1, xp=0, weekly_xp=0, wins=0, games=0, daily_challenges=0, list=[]):
        """Build a player with the given parameters. returns none if there are invalid parameters."""
        is_successful = True
        player = Player()
        is_successful = is_successful and player.set_name(name)
        is_successful = is_successful and player.set_gender(gender)
        is_successful = is_successful and player.set_avatar(avatar)
        is_successful = is_successful and player.set_level_xp(lvl, xp)
        is_successful = is_successful and player.set_weekly_xp(weekly_xp)
        is_successful = is_successful and player.set_wins(wins)
        is_successful = is_successful and player.set_games(games)
        is_successful = is_successful and player.set_daily_challenges(daily_challenges)
        is_successful = is_successful and player.set_achievement(list)
        return player if is_successful else None

    def set_name(self, name):
        """
        Sets Player's name, default = "No name"
        """
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            return True
        else:
            return False

    def set_avatar(self, avatar):
        """
        Sets Player's avatar image, default = None.
        """
        if avatar is not None or isinstance(avatar, str) and len(avatar) > 0:
            self._avatar = avatar
            return True
        elif avatar is None:
            self._avatar = "..\\storage\\icons\\default.jpg"
            return True
        else:
            return False

    def set_gender(self, gender):
        """
        Sets Player's gender, default = False.
        """
        if isinstance(gender, bool):
            self._gender = gender
            return True
        else:
            return False

    def set_weekly_xp(self, xp):
        if isinstance(xp, int) and xp >= 0:
            self._weekly_xp = xp
            return True
        else:
            return False

    def set_wins(self, wins):
        if isinstance(wins, int) and wins >= 0:
            self._wins = wins
            return True
        else:
            return False

    def set_games(self, games):
        if isinstance(games, int) and games >= 0:
            self._games = games
            return True
        else:
            return False

    def set_daily_challenges(self, d_ch):
        if isinstance(d_ch, int) and d_ch >= 0:
            self._daily_challenges = d_ch
            return True
        else:
            return False

    def get_gender(self):
        """Returns Male or Female"""
        return self._gender

    def get_weekly_xp(self):
        return self._weekly_xp

    def get_wins(self):
        return self._wins

    def get_games(self):
        return self._games

    def get_daily_challenges(self):
        return self._daily_challenges

    def get_achievements(self):
        return self.achievements

    def increase_xp(self, xp):
        """Takes xp and adds them to Player's current xp points."""
        if isinstance(xp, int) and xp >= 0:
            self._xp += xp
            self._level_up()  # reset level

    def increase_weekly_xp(self, xp):
        if isinstance(xp, int) and xp >= 0:
            print("weekly xp is increased by ", xp)
            self._weekly_xp += xp

    def increment_wins(self):
        self._wins += 1

    def increment_games(self):
        self._games += 1

    def report_game(self, is_win=0, gained_xp=0):
        self.increment_games()
        self.increase_xp(gained_xp)
        self.increase_weekly_xp(gained_xp)
        if is_win:
            self.increment_wins()
        self.update_achievements("game")
        self.update_achievements("xp")
        self.update_achievements("wins")
        self.update_achievements("level")

    def set_achievement(self, achievements_list):
        if isinstance(achievements_list, list) and achievements_list is not None:
            self.achievements = achievements_list
            return True
        return False

    def update_achievements(self, achievement_type):
        for achievement in self.achievements:
            achievement.update(achievement_type, self)
