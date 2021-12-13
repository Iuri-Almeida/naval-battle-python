from typing import List

from navalbattle.naval_battle_piece import NavalBattlePiece


class UI(object):

    __ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    @staticmethod
    def print_board(pieces: List[List[NavalBattlePiece]]):

        rows = len(pieces)
        columns = len(pieces[0])

        UI.__print_title('JOGADOR')

        print('|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')

        for i in range(rows):
            UI.__print_line()

            print(f'| {UI.__ROWS[i]} | ', end='')

            for j in range(columns):
                piece = pieces[i][j]
                print(f'{"  |" if piece is None else f"{piece} |"} ', end='')

            print()

        UI.__print_line()

    @staticmethod
    def __print_title(title: str) -> None:
        UI.__print_line()
        print(f'{title:^45}')
        UI.__print_line()

    @staticmethod
    def __print_line() -> None:
        print('-' * 45)
