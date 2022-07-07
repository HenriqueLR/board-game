from random import randint


class BoardDefault:

    owners: list = [None] * 20
    sale_value: list = [randint(30 + x, 100) for x in range(1, 21)]
    rent: list = [v * 0.5 for v in sale_value]

    @staticmethod
    def check_owners(board, position: int) -> bool:
        if board.owners[position] is not None:
            return False
