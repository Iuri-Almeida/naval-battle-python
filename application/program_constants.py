from application.ansi_color_constants import ANSIColorConstants


class ProgramConstants(object):

    # Board
    ROWS = 10
    COLUMNS = 10
    FIRST_ROW = 'a'
    LAST_ROW = 'j'
    ROW_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    # Game Colors
    PERSON_PIECE_COLOR = ANSIColorConstants.ANSI_PURPLE
    COMPUTER_PIECE_COLOR = ANSIColorConstants.ANSI_YELLOW
    INDICATORS_COLOR = ANSIColorConstants.ANSI_GREEN
    RESET_COLOR = ANSIColorConstants.ANSI_RESET

    # Game Numbers
    TOTAL_SUBMARINES = 10

    # Game Names
    PLAYER = 'PLAYER'
    PLAYER_SETUP = 'PLAYER (SETUP)'
    COMPUTER = 'COMPUTER'
