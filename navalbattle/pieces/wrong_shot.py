from navalbattle.naval_battle_piece import NavalBattlePiece
from navalbattle.player import Player


class WrongShot(NavalBattlePiece):

    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def __str__(self) -> str:
        return '-'
