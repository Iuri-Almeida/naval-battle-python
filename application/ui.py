from typing import List

from navalbattle.naval_battle_piece import NavalBattlePiece


class UI(object):

    @staticmethod
    def print_board(pieces: List[List[NavalBattlePiece]]):

        rows = len(pieces)
        columns = len(pieces[0])

        for i in range(rows):
            print(f'{rows - i - 1} ', end='')
            for j in range(columns):
                piece = pieces[i][j]
                print(f'{"-" if piece is None else piece} ', end='')
            print()
        print('  a b c d e f g h i j')
