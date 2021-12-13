class Position(object):

    def __init__(self, row: int, column: int) -> None:
        self.__row = row
        self.__column = column

    def __str__(self) -> str:
        return f'{self.__row}, {self.__column}'

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column
