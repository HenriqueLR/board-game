from player import NpcDefault
from random import randint


class NpcImpulsive(NpcDefault):
    behavior = "impulsive"

    def _buy(self, board, position: int, state: bool = False) -> bool:
        board.check_owners(board, position)
        sale_value = board.sale_value[position]
        if self._credit >= sale_value:
            self._credit -= sale_value
            state = True
        return state


class NpcDemanding(NpcDefault):
    behavior = "demanding"

    def _buy(self, board, position: int, state: bool = False) -> bool:
        board.check_owners(board, position)
        sale_value = board.sale_value[position]
        rent = board.rent[position]
        if self._credit >= sale_value and rent > 50:
            self._credit -= sale_value
            state = True
        return state


class NpcCautious(NpcDefault):
    behavior = "cautious"

    def _buy(self, board, position: int, state: bool = False) -> bool:
        board.check_owners(board, position)
        sale_value = board.sale_value[position]
        if self._credit >= sale_value and self._credit - sale_value > 80:
            self._credit -= sale_value
            state = True
        return state


class NpcRandom(NpcDefault):
    behavior = "random"

    def _buy(self, board, position: int, state: bool = False) -> bool:
        board.check_owners(board, position)
        sale_value = board.sale_value[position]
        choice = bool(randint(0, 1))
        if self._credit >= sale_value and choice is True:
            self._credit -= sale_value
            state = True
        return state
