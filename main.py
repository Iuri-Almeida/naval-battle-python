from application.ui import UI
from navalbattle.naval_battle_match import NavalBattleMatch


def main() -> None:
    match = NavalBattleMatch()

    while True:
        UI.print_board(match.get_pieces())
        target = UI.read_naval_battle_position('Target: ')

        match.perform_move(target)


if __name__ == '__main__':
    main()
