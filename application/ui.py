from typing import List

from application.program_constants import ProgramConstants
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.player import Player


class UI(object):

    __ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    @staticmethod
    def print_board(pieces: List[List[NavalBattlePiece]]):

        rows = len(pieces)
        columns = len(pieces[0])

        UI.__print_title('JOGADOR', ProgramConstants.PERSON_PIECE_COLOR)

        print(f'{ProgramConstants.INDICATORS_COLOR}|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |'
              f'{ProgramConstants.RESET_COLOR}')

        for i in range(rows):
            UI.__print_line(ProgramConstants.INDICATORS_COLOR)

            print(f'{ProgramConstants.INDICATORS_COLOR}| {UI.__ROWS[i]} | {ProgramConstants.RESET_COLOR}', end='')

            for j in range(columns):
                UI.__print_piece(pieces[i][j])

            print()

        UI.__print_line(ProgramConstants.INDICATORS_COLOR)

    @staticmethod
    def __print_piece(piece: NavalBattlePiece) -> None:
        if piece is None:
            print(f'{ProgramConstants.INDICATORS_COLOR}  |{ProgramConstants.RESET_COLOR}', end='')
        else:
            if piece.player == Player.PERSON:
                print(f'{ProgramConstants.PERSON_PIECE_COLOR}{piece}{ProgramConstants.INDICATORS_COLOR} |'
                      f'{ProgramConstants.RESET_COLOR}', end='')
            else:
                print(f'{ProgramConstants.COMPUTER_PIECE_COLOR}{piece}{ProgramConstants.INDICATORS_COLOR} |'
                      f'{ProgramConstants.RESET_COLOR}', end='')
        print(' ', end='')

    @staticmethod
    def __print_title(title: str, color: str) -> None:
        UI.__print_line(color)
        print(f'{color}{title:^45}{ProgramConstants.RESET_COLOR}')
        UI.__print_line(color)

    @staticmethod
    def __print_line(color: str) -> None:
        print(f'{color}{"-" * 45}{ProgramConstants.RESET_COLOR}')
