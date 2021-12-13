from typing import Optional, List

from boardgame.piece import Piece
from boardgame.position import Position


class Board(object):

    def __init__(self, rows: int, columns: int) -> None:
        self.__rows = rows
        self.__columns = columns
        self.__pieces: List[List[Optional[Piece]]] = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append(None)
            self.__pieces.append(row)

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    def piece(self, row: int, column: int) -> Piece:
        return self.__pieces[row][column]

    def piece_by_position(self, position: Position) -> Piece:
        return self.piece(position.row, position.column)
