from application.ui import UI
from boardgame.board_exception import BoardException
from navalbattle.naval_battle_match import NavalBattleMatch


def main() -> None:
    match = NavalBattleMatch()

    UI.setup_person_board(match)

    while not match.is_game_ended:
        try:
            UI.clear_screen()
            UI.print_match(match)

            target = UI.read_naval_battle_position('Target: ')

            match.perform_move(target)
        except (BoardException, ValueError) as e:
            print(f'{e}\n')
            input('Click ENTER to continue.')

    UI.clear_screen()
    UI.print_winner(match)


if __name__ == '__main__':
    main()
