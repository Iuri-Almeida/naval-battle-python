from typing import Optional, List

from boardgame.board_exception import BoardException
from boardgame.piece import Piece
from boardgame.position import Position
from navalbattle.pieces.right_shot import RightShot
from navalbattle.pieces.right_shot_with_submarine import RightShotWithSubmarine


class Board(object):

    def __init__(self, rows: int, columns: int) -> None:
        if rows < 1 or columns < 1:
            raise BoardException('Error creating board: there must be at least 1 row and 1 column.')

        self.__rows = rows
        self.__columns = columns
        self.__hits = 0
        self.__pieces: List[List[Optional[Piece]]] = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append(None)
            self.__pieces.append(row)

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    @property
    def hits(self) -> int:
        return self.__hits

    def piece(self, row: int, column: int) -> Piece:
        if not self.__position_exists(row, column):
            raise BoardException('Position not on the board.')

        return self.__pieces[row][column]

    def piece_by_position(self, position: Position) -> Piece:
        return self.piece(position.row, position.column)

    def place_piece(self, piece: Piece, position: Position) -> None:
        if self.there_is_a_piece(position):
            raise BoardException(f'There is already a piece on position: {position}')

        self.__pieces[position.row][position.column] = piece
        piece._position = position

    def place_piece_without_exception(self, piece: Piece, position: Position) -> None:
        if isinstance(piece, RightShot) or isinstance(piece, RightShotWithSubmarine):
            self.__hits += 1

        self.__pieces[position.row][position.column] = piece
        piece._position = position

    def __position_exists(self, row: int, column: int) -> bool:
        return 0 <= row < self.__rows and 0 <= column < self.__columns

    def position_exists_by_position(self, position: Position) -> bool:
        return self.__position_exists(position.row, position.column)

    def there_is_a_piece(self, position: Position) -> bool:
        if not self.position_exists_by_position(position):
            raise BoardException("Position not on the board.")

        return self.piece_by_position(position) is not None
