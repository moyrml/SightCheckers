from piece import Piece


class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = None

        self.initialize_board()

    def initialize_board(self):
        self.board = [[[] for _ in range(self.size)] for _ in range(self.size)]

        # initialize white pieces
        for x in range(0, self.size, 2):
            for y in range(0, self.size // 2 - 1):
                location = self.get_location(y, x + y % 2 + 1)
                self.board[location[0]][location[1]] = Piece(0, location)

        for x in range(0, self.size, 2):
            for y in range(self.size // 2 + 1, self.size):
                location = self.get_location(y, x + y % 2 + 1)
                self.board[location[0]][location[1]] = Piece(1, location)

    def get_location(self, x, y):
        """
        Translate between instructions indexing and pythons indexing.
        :param x: horizontal location relative to bottom right
        :param y: vertical location relative to bottom right
        :return: tuple. index in nested list structure.
        """

        rel_x = self.size - x - 1
        rel_y = self.size - y - 1

        return rel_x, rel_y

    def __repr__(self):
        out_str = ''
        for row in self.board:
            for col_item in row:
                to_append = ''
                if not col_item:
                    to_append = '-\t'
                else:
                    to_append = f'{col_item.__repr__()}\t'
                out_str += to_append
            out_str += '\n'
        return out_str


if __name__ == '__main__':
    board = Board()
    print(board)
    print('Done')
