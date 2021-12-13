from os import system
from typing import List

from application.program_constants import ProgramConstants
from boardgame.board_exception import BoardException
from navalbattle.naval_battle_match import NavalBattleMatch
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.naval_battle_position import NavalBattlePosition
from navalbattle.player import Player


class UI(object):

    __ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    @staticmethod
    def clear_screen() -> None:
        system('clear')

    @staticmethod
    def read_naval_battle_position(txt: str) -> NavalBattlePosition:
        try:
            s = input(f'\n{txt}').strip().lower()

            row = s[0]
            column = 10 - int(s[1:])

            return NavalBattlePosition(row, column)
        except (RuntimeError, IndexError):
            raise ValueError('Error reading Position. Valid values are from a0 to j9.')

    @staticmethod
    def setup_person_board(match: NavalBattleMatch) -> None:
        i = 0
        while i < ProgramConstants.TOTAL_SUBMARINES:
            try:
                UI.clear_screen()
                UI.__print_board(match.get_pieces(match.person_board), ProgramConstants.PLAYER_SETUP)

                target = UI.read_naval_battle_position('Target: ')

                match.perform_first_move(target)

                i += 1
            except (BoardException, ValueError) as e:
                print(f'{e}\n')
                input('Click ENTER to continue.')

    @staticmethod
    def print_winner(match: NavalBattleMatch) -> None:
        UI.__print_board(match.get_pieces(match.person_board), ProgramConstants.PLAYER)
        print()
        UI.__print_board(match.get_pieces(match.computer_board), ProgramConstants.COMPUTER)

        winner = match.current_player
        color = ProgramConstants.PERSON_PIECE_COLOR if winner == Player.PERSON else ProgramConstants.COMPUTER_PIECE_COLOR

        print(f'\nWinner: {color}{winner.name}{ProgramConstants.RESET_COLOR}')

    @staticmethod
    def print_match(match: NavalBattleMatch):
        UI.__print_board(match.get_pieces(match.person_board), ProgramConstants.PLAYER)
        print(f'\nTurn: {match.turn}')

    @staticmethod
    def __print_board(pieces: List[List[NavalBattlePiece]], title: str):

        rows = len(pieces)
        columns = len(pieces[0])

        UI.__print_title(title, ProgramConstants.PERSON_PIECE_COLOR)

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
