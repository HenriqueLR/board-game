import random
from player.npc import NpcImpulsive, NpcDemanding, NpcCautious, NpcRandom
from board.default import BoardDefault


def set_player_board():
    board = BoardDefault()
    players = [NpcImpulsive(), NpcDemanding(), NpcCautious(), NpcRandom()]
    random.shuffle(players)
    return board, players
