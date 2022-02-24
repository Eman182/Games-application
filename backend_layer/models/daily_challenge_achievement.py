from backend_layer.models.achievements import AchievementInterface


class DailyChallengeAchievement(AchievementInterface):

    def __init__(self, ach_id, description, checked, goal):
        self.ach_id = ach_id
        self.description = description
        self.checked = checked
        self.goal = goal

    def __eq__(self, other):
        if not isinstance(other, DailyChallengeAchievement):
            return NotImplemented

        return self.ach_id == other.ach_id and self.description == other.description and self.checked == other.checked and self.goal == other.goal

    def get_id(self):
        return self.ach_id

    def get_description(self):
        return self.description

    def get_checked(self):
        return self.checked

    def get_reward(self):
        return self.goal * 7

    def update(self, achievement_type, player):
        if achievement_type == "daily challenge" and player.get_daily_challenges() >= self.goal and self.checked == 0:
            self.checked = 1
            player.increase_xp(self.get_reward())
            player.increase_weekly_xp(self.get_reward())
