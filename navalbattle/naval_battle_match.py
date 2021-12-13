from random import choice, randint
from string import ascii_lowercase
from typing import List, Optional, cast

from application.program_constants import ProgramConstants
from boardgame.board import Board
from boardgame.position import Position
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.naval_battle_position import NavalBattlePosition
from navalbattle.pieces.right_shot import RightShot
from navalbattle.pieces.right_shot_with_submarine import RightShotWithSubmarine
from navalbattle.pieces.submarine import Submarine
from navalbattle.pieces.wrong_shot import WrongShot
from navalbattle.pieces.wrong_shot_with_submarine import WrongShotWithSubmarine
from navalbattle.player import Player


class NavalBattleMatch(object):

    __POSITIONS_ALREADY_VERIFIED: List[str] = []

    def __init__(self) -> None:
        self.__person_board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)
        self.__computer_board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)
        self.__turn = 1
        self.__current_player = Player.PERSON
        self.__game_ended = False

        self.__initial_setup()

    @property
    def person_board(self) -> Board:
        return self.__person_board

    @property
    def computer_board(self) -> Board:
        return self.__computer_board

    @property
    def turn(self) -> int:
        return self.__turn

    @property
    def current_player(self) -> Player:
        return self.__current_player

    @property
    def is_game_ended(self) -> bool:
        return self.__game_ended

    def get_pieces(self, board: Board) -> List[List[NavalBattlePiece]]:
        rows = board.rows
        columns = board.columns

        pieces: List[List[Optional[NavalBattlePiece]]] = []

        for i in range(rows):
            row: List[NavalBattlePiece] = []
            for j in range(columns):
                row.append(cast(NavalBattlePiece, board.piece(i, j)))
            pieces.append(row)

        return pieces

    def perform_first_move(self, target_position: NavalBattlePosition) -> None:
        target = target_position.to_position()
        self.__person_board.place_piece(Submarine(self.__person_board, Player.PERSON), target)

    def perform_move(self, target_position: NavalBattlePosition) -> None:
        target = target_position.to_position()
        self.__make_move(target, self.__person_board)

        self.__game_ended = self.__test_end_of_game(self.__person_board)

        if not self.__game_ended:
            self.__next_turn()
            self.__perform_computer_move()

    def __perform_computer_move(self) -> None:
        row = self.__generate_random_char()
        column = self.__generate_random_int()
        pos = f'{row}{column}'

        while pos in self.__POSITIONS_ALREADY_VERIFIED:
            row = self.__generate_random_char()
            column = self.__generate_random_int()
            pos = f'{row}{column}'

        self.__POSITIONS_ALREADY_VERIFIED.append(pos)

        target = NavalBattlePosition(row, column).to_position()

        self.__make_move(target, self.__computer_board)

        self.__game_ended = self.__test_end_of_game(self.__computer_board)

        if not self.__game_ended:
            self.__next_turn()

    def __make_move(self, target: Position, board: Board) -> None:
        if board == self.__person_board:
            other_board = self.__computer_board
            player = Player.PERSON
        else:
            other_board = self.__person_board
            player = Player.COMPUTER

        if other_board.there_is_a_piece(target) and (isinstance(other_board.piece_by_position(target), Submarine) or
                                                     isinstance(other_board.piece_by_position(target), WrongShotWithSubmarine)):
            if board.there_is_a_piece(target) and (isinstance(board.piece_by_position(target), Submarine) or
                                                   isinstance(board.piece_by_position(target), RightShotWithSubmarine)):
                board.place_piece_without_exception(RightShotWithSubmarine(board, player), target)
            else:
                board.place_piece_without_exception(RightShot(board, player), target)
        else:
            if board.there_is_a_piece(target) and (isinstance(board.piece_by_position(target), Submarine) or
                                                   isinstance(board.piece_by_position(target), WrongShotWithSubmarine)):
                board.place_piece_without_exception(WrongShotWithSubmarine(board, player), target)
            else:
                board.place_piece_without_exception(WrongShot(board, player), target)

    def __next_turn(self) -> None:
        self.__turn += 1
        self.__current_player = Player.COMPUTER if self.__current_player == Player.PERSON else Player.PERSON

    def __test_end_of_game(self, board: Board) -> bool:
        return board.hits == ProgramConstants.TOTAL_SUBMARINES

    def __generate_random_char(self) -> str:
        return choice(ascii_lowercase[:10])

    def __generate_random_int(self) -> int:
        return randint(1, 10)

    def __place_new_piece(self, row: str, column: int, piece: NavalBattlePiece) -> None:
        self.__computer_board.place_piece(piece, NavalBattlePosition(row, column).to_position())

    def __initial_setup(self) -> None:
        i = 0
        while i < ProgramConstants.TOTAL_SUBMARINES:
            row = self.__generate_random_char()
            column = self.__generate_random_int()

            position = NavalBattlePosition(row, column).to_position()

            if not self.__computer_board.there_is_a_piece(position):
                self.__place_new_piece(row, column, Submarine(self.__computer_board, Player.COMPUTER))
                i += 1
