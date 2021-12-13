from boardgame.board import Board
from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.player import Player


class WrongShot(NavalBattlePiece):

    def __init__(self, board: Board, player: Player) -> None:
        super().__init__(board, player)

    def __str__(self) -> str:
        return '-'
