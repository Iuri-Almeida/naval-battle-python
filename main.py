from application.ui import UI
from navalbattle.naval_battle_match import NavalBattleMatch


def main() -> None:
    match = NavalBattleMatch()
    UI.print_board(match.get_pieces())


if __name__ == '__main__':
    main()
