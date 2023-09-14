from __future__ import annotations

from enum import Enum, IntEnum, IntFlag


class CollisionFlag(IntFlag):
    NONE = 0
    BALL = 1
    RED = 2
    BLUE = 4
    REDKO = 8
    BLUEKO = 16
    WALL = 32
    ALL = 63
    KICK = 64
    SCORE = 128
    C0 = 268435456
    C1 = 536870912
    C2 = 1073741824
    C3 = -2147483648

    @staticmethod
    def from_list(collision_list: list[str]) -> CollisionFlag:
        if collision_list is None:
            raise ValueError("collision_list is None")

        return CollisionFlag(sum([DICT_COLLISION[c] for c in collision_list]))


class TeamID(IntEnum):
    SPECTATOR = 0
    RED = 1
    BLUE = 2


class GameState(IntEnum):
    KICKOFF = 0
    PLAYING = 1
    GOAL = 2
    END = 3


class ActionBin(IntEnum):
    RIGHT = 0
    UP = 1
    KICK = 2


class Input(IntEnum):
    UP = 4
    DOWN = 1
    LEFT = 2
    RIGHT = 8
    SHOOT = 16


class BaseMap(str, Enum):
    CLASSIC = "classic.json5"
    ROUNDED = "rounded.json5"
    BIG = "big.json5"
    FUTSAL_CLASSIC = "futsal-classic.json5"
    FUTSAL_BIG = "futsal-big.json5"
    PENALTY = "penalty-soccer.json5"
    OBSTACLE_WINKY = "obstacle-map-winky.json5"


class TeamColor(str, Enum):
    RED = "E56E56"
    BLUE = "5689E5"


GRASS_BORDER_COLOR = "C7E6BD"
HOCKEY_BORDER_COLOR = "E9CC6E"
DEFAULT_BORDER_COLOR = "000000"

GRASS_FILL_COLOR = "718C5A"
HOCKEY_FILL_COLOR = "555555"
DEFAULT_FILL_COLOR = "000000"


DICT_COLLISION = {
    "": CollisionFlag.NONE,
    "ball": CollisionFlag.BALL,
    "red": CollisionFlag.RED,
    "blue": CollisionFlag.BLUE,
    "redKO": CollisionFlag.REDKO,
    "blueKO": CollisionFlag.BLUEKO,
    "wall": CollisionFlag.WALL,
    "all": CollisionFlag.ALL,
    "kick": CollisionFlag.KICK,
    "score": CollisionFlag.SCORE,
    "c0": CollisionFlag.C0,
    "c1": CollisionFlag.C1,
    "c2": CollisionFlag.C2,
    "c3": CollisionFlag.C3,
}

DICT_KEYS = {
    "bCoef": "bouncing_coefficient",
    "cGroup": "collision_group",
    "cMask": "collision_mask",
    "radius": "radius",
    "invMass": "inverse_mass",
    "damping": "damping",
    "curve": "curve",
    "curveF": "_curveF",
    "bias": "bias",
    "vis": "visible",
    "color": "color",
    "spawnDistance": "spawn_distance",
    "kickOffRadius": "kickoff_radius",
    "cornerRadius": "corner_radius",
    "pos": "position",
    "dist": "distance_origin",
    "vertexes": "vertices",
    "bg": "background",
    "goalLine": "goal_line",
    "speed": "velocity",
    "cameraWidth": "camera_width",
    "cameraHeight": "camera_height",
}
