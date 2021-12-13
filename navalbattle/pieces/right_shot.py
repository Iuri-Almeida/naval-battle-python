from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.player import Player


class RightShot(NavalBattlePiece):

    def __init__(self, board, player: Player) -> None:
        super().__init__(board, player)

    def __str__(self) -> str:
        return '*'
