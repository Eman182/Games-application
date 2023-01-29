from player import Player
from xp_achievement import XpAchievement
from wins_achievement import WinsAchievement
from level_achievement import LevelAchievement

player = Player.build_player("nour waled",[])
list = [XpAchievement("reach xp 2",0,player), WinsAchievement("reach xp 3",0,player)]
player.set_achievement(list)
player.set_level_xp(1,5)
print(list[0].checked)
player. update_achievements("xp")
print(list[0].checked)
print(list[1].checked)