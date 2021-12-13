from typing import List, Optional, cast

from boardgame.board import Board
from navalbattle.naval_battle_piece import NavalBattlePiece


class NavalBattleMatch(object):

    def __init__(self) -> None:
        self.__board = Board(10, 10)

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
