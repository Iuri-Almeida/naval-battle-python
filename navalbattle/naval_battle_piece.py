from boardgame.piece import Piece
from navalbattle.player import Player


class NavalBattlePiece(Piece):

    def __init__(self, board, player: Player) -> None:
        super().__init__(board)
        self.__player = player

    @property
    def player(self) -> Player:
        return self.__player
