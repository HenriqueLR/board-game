import collections


def format_results_players(prop):
    impulsive = round(prop["impulsive"] / 300 * 100, 2)
    demanding = round(prop["demanding"] / 300 * 100, 2)
    cautious = round(prop["cautious"] / 300 * 100, 2)
    random = round(prop["random"] / 300 * 100, 2)
    return impulsive, demanding, cautious, random


def format_results_rounds(prop):
    return round(prop / 300, 2)


def show(prop: dict) -> print:
    rounds = format_results_rounds(prop.get("rounds"))
    timeouts = prop.get("timeouts")
    players = collections.Counter(prop.get("players"))
    impulsive, demanding, cautious, random = format_results_players(players)
    print("######## RESULTS ########")
    print(f"All timeouts: {timeouts}")
    print(f"AVG rounds of a match: {rounds}")
    print("Percentage of wins behavior:")
    print(f"-> impulsive: {impulsive}%")
    print(f"-> demanding: {demanding}%")
    print(f"-> cautious: {cautious}%")
    print(f"-> random: {random}%")
    print(f"Behavior max win: {max(players, key=players.get)}")
