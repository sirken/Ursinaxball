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
player_blue = PlayerHandler("P2", TeamID.BLUE)
bot_blue1 = PlayerHandler("b1", TeamID.BLUE, bot=bot_blue)
bot_red1 = PlayerHandler("r1", TeamID.RED, bot=bot_red)

game.add_players([player_red, player_blue, bot_red1, bot_blue1])


@dataclass
class InputPlayer:
    left: list[str]
    right: list[str]
    up: list[str]
    down: list[str]
    shoot: list[str]


input_player1 = InputPlayer(
    left=[Keys.left_arrow],
    right=[Keys.right_arrow],
    up=[Keys.up_arrow],
    down=[Keys.down_arrow],
    shoot=["/"],
)

input_player2 = InputPlayer(
    left=["a"],
    right=["d"],
    up=["w"],
    down=["s"],
    shoot=[Keys.left_shift],
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
    actions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while not done:
        actions[0] = action_handle(actions[0], input_player1)
        actions[1] = action_handle(actions[1], input_player2)
        actions[2] = bot_red1.step(game)
        actions[3] = bot_blue1.step(game)
        done = game.step(actions)
