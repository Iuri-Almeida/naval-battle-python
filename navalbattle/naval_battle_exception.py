from boardgame.board_exception import BoardException


class NavalBattleException(BoardException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
