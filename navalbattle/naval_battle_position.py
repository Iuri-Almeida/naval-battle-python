from application.program_constants import ProgramConstants
from boardgame.position import Position
from navalbattle.naval_battle_exception import NavalBattleException


class NavalBattlePosition(object):

    def __init__(self, row: str, column: int) -> None:
        if row < ProgramConstants.FIRST_ROW or row > ProgramConstants.LAST_ROW \
                or column < 0 or column > ProgramConstants.COLUMNS:
            raise NavalBattleException('Error instantiating Position. Valid values are from a0 to j9.')

        self.__row = row
        self.__column = column

    def __str__(self) -> str:
        return f'{self.__row}{self.__column}'

    def to_position(self) -> Position:
        row = ProgramConstants.ROW_CHARS.index(self.__row) - ProgramConstants.ROW_CHARS.index(ProgramConstants.FIRST_ROW)
        column = ProgramConstants.COLUMNS - self.__column

        return Position(row, column)
