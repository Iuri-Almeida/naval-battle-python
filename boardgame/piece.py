from typing import Optional

from boardgame.position import Position


class Piece(object):

    def __init__(self) -> None:
        self._position: Optional[Position] = None
