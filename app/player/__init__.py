from utils.square import cast_square
from abc import ABC, abstractmethod


class NpcDefault(ABC):

    def __init__(self) -> None:
        self.disabled: bool = False
        self._credit: int = 300
        self._position: int = 0
        self._properts: list = []

    @abstractmethod
    def _buy(self, board, position: int) -> bool:
        raise NotImplementedError()

    def _pay_rent(self, board, position: int, state: bool = False) -> bool:
        rent = board.rent[position]
        if self._credit >= rent:
            self._credit -= rent
            state = True
        return state

    def play(self, board, index: int, state: bool = True) -> bool:
        self._position += cast_square()
        len_board = len(board.sale_value) - 1
        if self._position > len_board:
            self._credit += 100
            self._position -= len_board
        if board.owners[self._position] is None and self._buy(board, self._position):
            self._properts.append(self._position)
            board.owners[self._position] = index
        else:
            if board.owners[self._position] is not None and self._position not in self._properts:
                if not self._pay_rent(board, self._position):
                    self.disabled = True
                    state = False
        return state
