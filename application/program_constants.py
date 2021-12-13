from application.ansi_color_constants import ANSIColorConstants


class ProgramConstants(object):

    # Board
    ROWS = 10
    COLUMNS = 10
    FIRST_ROW = 'a'
    LAST_ROW = 'j'

    # Game Colors
    PERSON_PIECE_COLOR = ANSIColorConstants.ANSI_PURPLE
    COMPUTER_PIECE_COLOR = ANSIColorConstants.ANSI_YELLOW
    INDICATORS_COLOR = ANSIColorConstants.ANSI_GREEN
    RESET_COLOR = ANSIColorConstants.ANSI_RESET
