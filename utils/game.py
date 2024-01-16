from utils.board import Board
from utils.errors import IllegalMoveException


class Game:
    def __init__(self):
        self.board = Board()
        self.n_moves = None

    def start(self):
        self.n_moves = 0
        self.board.initialize_board()

    def make_move(self, move):
        capture_options = self.check_legality(move)
        self.board.move(move[:2], move[2:])

        if capture_options:
            captured_piece = capture_options[(move[2], move[3])]
            del self.board[captured_piece]

        self.n_moves += 1

    def check_legality(self, move):
        """
        Check weather a move is legal or not. If not - raise exception, otherwise return the capture options
        :param move: tuple: (int, int, int, int)
        :return: list of tuples. Capture options
        :raise: errors.IllegalMoveException in the case of an illegal move
        """
        x0, y0, x1, y1 = move
        moving_piece = self.board[x0, y0]
        can_capture = moving_piece.can_capture(self.board)

        rules_broken = [
            self.n_moves == 0 and moving_piece.color != 0,  # starting piece is not white
            x1 >= self.board.size or y1 >= self.board.size,  # a move to outside the board
            len(can_capture) > 0 and (x1, y1) not in can_capture,  # can capture but next move s not a capture
            not can_capture and x0 - x1 not in [-1, 1],  # The move is not in a diagonal with 1 jump and not a capture
            not can_capture and y1 - y0 != 1 - 2 * moving_piece.color,  # The move is not "forward"
            bool(self.board[move[2:]])
        ]

        if any(rules_broken):
            raise IllegalMoveException(move)

        return can_capture




if __name__ == '__main__':
    game = Game()
    game.start()
    game.make_move((1,2,2,3))