from typing import Optional, List

from boardgame.piece import Piece


class Board(object):

    def __init__(self, rows: int, columns: int) -> None:
        self.__rows = rows
        self.__columns = columns
        self.__pieces: List[List[Optional[Piece]]] = [[None] * columns] * rows

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns
