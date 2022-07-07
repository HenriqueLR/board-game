from match.session import start
from utils.info import show


def main():
    all_timeouts, all_rounds, players = 0, 0, []
    for i in range(300):
        instance = start()
        players.append(instance.get("player"))
        all_rounds += instance.get("rounds")
        if instance.get("timeout") is True:
            all_timeouts += 1
    show({'rounds': all_rounds, 'players': players, 'timeouts': all_timeouts})


if __name__ == '__main__':
    main()
