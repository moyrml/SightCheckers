from utils.game import Game
import sys
from pathlib import Path
from utils.report_progression import report_progression, reset_progression

if __name__ == '__main__':
    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        print("""
        How to use:
        >>> python main.py [-h,--help] [-v,--verbose] /path/to/moves_file.txt
        
        -h, --help: Optional. Print this and exit.
        -v, --verbose: Optional. Create a txt file depicting step-by-step game progress.
        """)

        sys.exit(1)

    verbose = False
    if '-v' in sys.argv or '--verbose' in sys.argv:
        verbose = True
        reset_progression()

    moves_file = Path(sys.argv[-1])
    assert moves_file.exists(), f"Cannot find moves file at {moves_file}"

    with open(moves_file) as f:
        moves = f.read().splitlines()

    game = Game()
    game.start()
    if verbose:
        report_progression(game, 0)

    for line_no, move in enumerate(moves):
        move = [int(i) for i in move.split(',')]
        game.make_move(move)

        if verbose:
            report_progression(game, line_no+1, move)

    print('Done')
