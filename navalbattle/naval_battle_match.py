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
        self.__board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)

        self.__initial_setup()

    def get_pieces(self) -> List[List[NavalBattlePiece]]:

        rows = self.__board.rows
        columns = self.__board.columns

        pieces: List[List[Optional[NavalBattlePiece]]] = []

        for i in range(rows):
            row: List[NavalBattlePiece] = []
            for j in range(columns):
                row.append(cast(NavalBattlePiece, self.__board.piece(i, j)))
            pieces.append(row)

        return pieces

    def perform_move(self, target_position: NavalBattlePosition) -> None:
        target = target_position.to_position()
        self.__make_move(target)

    def __make_move(self, target: Position) -> None:
        self.__board.place_piece(Submarine(self.__board, Player.PERSON), target)

    def __place_new_piece(self, row: str, column: int, piece: NavalBattlePiece) -> None:
        self.__board.place_piece(piece, NavalBattlePosition(row, column).to_position())

    def __initial_setup(self) -> None:
        pass
