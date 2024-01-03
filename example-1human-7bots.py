from dataclasses import dataclass

from ursina import Keys, held_keys

from ursinaxball import Game
from ursinaxball.common_values import BaseMap, TeamID
from ursinaxball.modules import GameScore, PlayerHandler, ChaseBot

game = Game(
    folder_rec="./recordings/",
    enable_vsync=True,
    stadium_file=BaseMap.CLASSIC,
)
game.score = GameScore(time_limit=5, score_limit=10)
tick_skip = 2

bot_blue = ChaseBot(tick_skip)
bot_red = ChaseBot(tick_skip)

player_red = PlayerHandler("P1", TeamID.RED)
bot_blue1 = PlayerHandler("bot_blue1", TeamID.BLUE, bot=bot_blue)
bot_red1 = PlayerHandler("bot_red1", TeamID.RED, bot=bot_red)
bot_blue2 = PlayerHandler("bot_blue2", TeamID.BLUE, bot=bot_blue)
bot_red2 = PlayerHandler("bot_red2", TeamID.RED, bot=bot_red)
bot_blue3 = PlayerHandler("bot_blue3", TeamID.BLUE, bot=bot_blue)
bot_red3 = PlayerHandler("bot_red3", TeamID.RED, bot=bot_red)
bot_blue4 = PlayerHandler("bot_blue4", TeamID.BLUE, bot=bot_blue)
game.add_players([player_red, bot_blue1, bot_red1, bot_blue2, bot_red2, bot_blue3, bot_red3, bot_blue4])


@dataclass
class InputPlayer:
    left: list[str]
    right: list[str]
    up: list[str]
    down: list[str]
    shoot: list[str]


input_player = InputPlayer(
    left=[Keys.left_arrow],
    right=[Keys.right_arrow],
    up=[Keys.up_arrow],
    down=[Keys.down_arrow],
    shoot=["x"],
)


def action_handle(actions_player_output: list[int], inputs_player: InputPlayer):
    actions_player_output = [0, 0, 0]
    for key, value in held_keys.items():
        if value != 0:
            if key in inputs_player.left:
                actions_player_output[0] -= 1
            if key in inputs_player.right:
                actions_player_output[0] += 1
            if key in inputs_player.up:
                actions_player_output[1] += 1
            if key in inputs_player.down:
                actions_player_output[1] -= 1
            if key in inputs_player.shoot:
                actions_player_output[2] += 1
    return actions_player_output


while True:
    save_rec = False
    game.reset(save_recording=save_rec)
    done = False
    actions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while not done:
        actions[0] = action_handle(actions[0], input_player)
        actions[1] = bot_blue1.step(game)
        actions[2] = bot_red1.step(game)
        actions[3] = bot_blue2.step(game)
        actions[4] = bot_red2.step(game)
        actions[5] = bot_blue3.step(game)
        actions[6] = bot_red3.step(game)
        actions[7] = bot_blue4.step(game)
        done = game.step(actions)
