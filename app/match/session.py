from utils.match import set_player_board


def start() -> dict:
    board, players = set_player_board()
    round: int = 0
    finish: bool = False

    while finish is False:
        for index, player in enumerate(players):
            round += 1
            if round >= 1000:
                return {"player": player.behavior, "timeout": True, "rounds": round}
            elif player.disabled is False and not player.play(board, index):
                player.disabled = True
                round += 1
        champion = [not(instance.disabled) for instance in players]
        if sum(champion) == 1:
            return {"player": players[champion.index(True)].behavior,
                    "timeout": False, "rounds": round}
