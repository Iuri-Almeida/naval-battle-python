from typing import Optional

from boardgame.position import Position


class Piece(object):

    def __init__(self, board) -> None:
        self.__board = board
        self._position: Optional[Position] = None

    @property
    def _board(self):
        return self.__board
