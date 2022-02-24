class Guest:
    """
       A class to represent a player.
       ...
       Attributes
       ----------
       _name : str
           player's user name. uniquely identifies a player
       _avatar : str
           a path (relative to project directory) to the player's avatar image
       _lvl : int
           player's current level. minimum = 1
       _xp : int
           player's xp points in the current level. minimum = 1
       _max_lvl_xp : int
           maximum xp points in the current level. used to calculate the next level's max xp
       Methods
       -------
       set_level_xp(level, xp):
           Returns True if level and xp are valid, False otherwise
       get_name():
           Returns player's name
       get_avatar():
           Returns player's avatar
       get_level():
           Returns player's level
       get_xp():
           Returns player's xp
       increase_xp(xp_points):
           Adds xp_points to player's xp and resets level
       __level_up():
           Increments player's level if needed
       __xp_to_complete():
           Returns the remaining xp points to complete the current level
       """

    def __init__(self):
        self._name = "Guest"
        self._avatar = "..\\storage\\icons\\default.jpg"
        self._lvl = 1
        self._xp = 0
        self._max_lvl_xp = 50

    @staticmethod
    def build_guest(name, gender=False, lvl=1, xp=0):
        """Build a guest player with the given parameters. returns none if there are invalid parameters."""
        is_successful = True
        guest = Guest()
        is_successful = is_successful and guest.set_name(name)
        # is_successful = is_successful and guest.set_avatar(avatar)
        is_successful = is_successful and guest.set_level_xp(lvl, xp)
        return guest if is_successful else None

    def set_name(self, name):
        """
            Sets Guest's name, default = "Guest"
        """
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            return True
        else:
            return False

    def set_level_xp(self, level, xp):  # level and xp have to be set together
        """
        Sets Player's level and xp, default level = 1, default xp = 0.
        """
        if isinstance(level, int) and level > 0 and isinstance(xp, int) and xp >= 0:
            self._lvl = level
            self._max_lvl_xp = 25 * self._lvl * (1+self._lvl)
            self._xp = xp
            self._level_up()
            return True
        else:
            return False

    def get_name(self):
        """Returns Player's name"""
        return self._name

    def get_avatar(self):
        """Returns Player's avatar image path (relative to project directory)"""
        return self._avatar

    def get_level(self):
        """Returns Player's current level"""
        return self._lvl

    def get_xp(self):
        """Returns Player's xp points withing the current level"""
        return self._xp

    def get_level_progress(self):
        """Returns Player's level progress percentage as a number from 0 to 100"""
        return 100*self._xp/self._max_lvl_xp

    def increase_xp(self, xp):
        """Takes xp and adds them to Player's current xp points."""
        if isinstance(xp, int) and xp >= 0:
            self._xp += xp
            self._level_up()  # reset level

    def _level_up(self):
        """Increments Player's level if it has enough xp points"""
        while self._xp >= self._max_lvl_xp:
            self._xp -= self._max_lvl_xp
            self._lvl += 1  # increment level
            self._max_lvl_xp = 25 * self._lvl * (1 + self._lvl)  # update level maximum xp level

    def xp_to_complete(self):
        """Returns remaining xp to complete the level."""
        return self._max_lvl_xp - self._xp

    def report_game(self, is_win=0, gained_xp=0):
        self.increase_xp(gained_xp)

    def reset(self):
        self._lvl = 1
        self._xp = 0
