from typing import List, Optional, cast

from boardgame.board import Board
from boardgame.position import Position
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.pieces.submarine import Submarine
from navalbattle.player import Player


class NavalBattleMatch(object):

    def __init__(self) -> None:
        self.__board = Board(10, 10)

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

    def __initial_setup(self) -> None:
        self.__board.place_piece(Submarine(self.__board, Player.PERSON), Position(1, 1))
        self.__board.place_piece(Submarine(self.__board, Player.PERSON), Position(2, 1))
        self.__board.place_piece(Submarine(self.__board, Player.PERSON), Position(0, 1))
