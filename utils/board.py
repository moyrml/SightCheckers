from piece import Piece


class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = None

        self.initialize_board()

    def initialize_board(self):
        self.board = [[[] for _ in range(self.size)] for _ in range(self.size)]

        # initialize white pieces
        locations = []
        for y in range(0, self.size // 2 - 1):
            for x in range(1 - y % 2, self.size + 1 - y % 2, 2):
                location = self.get_location(x, y)
                locations.append(location)
                self.board[location[1]][location[0]] = Piece(0, (x, y))

        # Now we do a trick. Since the board is reversible (it look the same from both players perspectives aside for
        # the color, and the coordinates are perfectly reversible w.r.t to the board size, we can inverse the locations
        # instead of re-calculating them
        for location in locations:
            inv_location = self.get_location(location[0], location[1])
            self.board[inv_location[1]][inv_location[0]] = Piece(1, (location[0], location[1]))

    def get_location(self, x, y):
        """
        Translate between instructions indexing to pythons indexing. Since the board is symmetric, this function
        is reversible.
        :param x: horizontal location relative to bottom right
        :param y: vertical location relative to bottom right
        :return: tuple. index in nested list structure.
        """

        rel_x = self.size - x - 1
        rel_y = self.size - y - 1

        return rel_x, rel_y

    def __getitem__(self, key):
        """

        :param key: Tuple of two items in the instructions coord system
        :return:
        """
        y, x = key
        rel_y, rel_x = self.get_location(x, y)
        return self.board[rel_y][rel_x]

    def __setitem__(self, key, value):
        y, x = key
        rel_y, rel_x = self.get_location(x, y)
        self.board[rel_y][rel_x] = value

    def __delitem__(self, key):
        y, x = key
        rel_y, rel_x = self.get_location(x, y)
        del self.board[rel_y][rel_x]

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
