def report_progression(game, lineno, move='', output_file='game_progression.txt'):
    with open(output_file, 'a') as f:
        f.write(f'move #{lineno}: {",".join([str(s) for s in move]):=<50}\n{game.board}\n')


def reset_progression(output_file='game_progression.txt'):
    with open(output_file, 'w') as f:
        pass
