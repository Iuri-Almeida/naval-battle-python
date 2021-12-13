from typing import List, Optional, cast

from application.program_constants import ProgramConstants
from boardgame.board import Board
from boardgame.position import Position
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.naval_battle_position import NavalBattlePosition
from navalbattle.pieces.submarine import Submarine
from navalbattle.player import Player


class NavalBattleMatch(object):

    def __init__(self) -> None:
        self.__person_board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)
        self.__computer_board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)
        self.__turn = 1
        self.__current_player = Player.PERSON

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

    def perform_move(self, target_position: NavalBattlePosition) -> None:
        target = target_position.to_position()
        self.__make_move(target)
        self.__next_turn()

    def __make_move(self, target: Position) -> None:
        self.__person_board.place_piece(Submarine(self.__person_board, Player.PERSON), target)

    def __next_turn(self) -> None:
        self.__turn += 1
        self.__current_player = Player.COMPUTER if self.__current_player == Player.PERSON else Player.PERSON

    def __place_new_piece(self, row: str, column: int, piece: NavalBattlePiece) -> None:
        self.__computer_board.place_piece(piece, NavalBattlePosition(row, column).to_position())

    def __initial_setup(self) -> None:
        self.__place_new_piece('a', 1, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('b', 2, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('c', 3, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('d', 4, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('e', 5, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('f', 6, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('g', 7, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('h', 8, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('i', 9, Submarine(self.__computer_board, Player.COMPUTER))
        self.__place_new_piece('j', 10, Submarine(self.__computer_board, Player.COMPUTER))
