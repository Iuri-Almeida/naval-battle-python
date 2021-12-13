from application.ui import UI
from boardgame.board_exception import BoardException
from navalbattle.naval_battle_match import NavalBattleMatch


def main() -> None:
    match = NavalBattleMatch()

    while True:
        try:
            UI.print_board(match.get_pieces())
            target = UI.read_naval_battle_position('Target: ')

            match.perform_move(target)
        except (BoardException, ValueError) as e:
            print(f'{e}\n')
            input('Click ENTER to continue.')


if __name__ == '__main__':
    main()
