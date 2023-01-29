from backend_layer.models.achievements import AchievementInterface


class LevelAchievement(AchievementInterface):

    def __init__(self, ach_id, description, checked, goal):
        self.ach_id = ach_id
        self.description = description
        self.goal = goal
        self.checked = checked

    def __eq__(self, other):
        if not isinstance(other, LevelAchievement):
            return NotImplemented

        return self.ach_id == other.ach_id and self.description == other.description and self.checked == other.checked and self.goal == other.goal

    def get_id(self):
        return self.ach_id

    def get_description(self):
        return self.description

    def get_checked(self):
        return self.checked

    def get_reward(self):
        return self.goal * 10

    def update(self, achievement_type, player):
        if achievement_type == "level" and player.get_level() >= self.goal and self.checked == 0:
            self.checked = 1
            player.increase_xp(self.get_reward())
            player.increase_weekly_xp(self.get_reward())
