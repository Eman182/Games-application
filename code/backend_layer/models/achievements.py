import abc


class AchievementInterface(abc.ABC):

    def get_id(self):
        pass

    def get_description(self):
        pass

    def get_checked(self):
        pass

    def get_reward(self):
        pass

    # to notify
    def update(self, achievement_type, player):
        pass
