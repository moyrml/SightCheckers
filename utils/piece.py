class Piece:
    def __init__(self, color, location, colors=('white', 'black')):
        """

        :param color: int. Location of this pieces color in colors
        :param location: list of size 2.
        :param colors: list. Human-readable colors.
        """
        self.color = color
        self.location = location
        self.colors = colors

    def __repr__(self):
        return self.colors[self.color][0]

    def __str__(self):
        return f'{self.colors[self.color]} piece at location {self.location}'

    def can_capture(self, board):
        """
        Checks if a piece can capture another piece, and return the capture end positions

        :param board: Pointer to the board
        :return: tuple. Positions at the end of the capture if can capture, [(-1, -1)] otherwise
        """
        # positions = set()
        captured_positions = dict()

        neighbors_1st_order_coords, neighbors_1st_order = self.get_forward_neighbors(board)
        for i, n1 in enumerate(neighbors_1st_order):
            if not n1:
                # First neighboring position is empty
                continue

            neighbors_2st_order_coords, neighbors_2st_order = n1.get_forward_neighbors(board)
            for j, n2 in enumerate(neighbors_2st_order):
                if not n2:
                    # Second neighboring position is empty
                    # positions.add(neighbors_2st_order_coords[j])
                    captured_positions[neighbors_2st_order_coords[j]] = n1.location

        return captured_positions

    def get_forward_neighbors(self, board):
        neighbors_coords = [
            [self.location[0] + 1, self.location[1] + 1 - 2 * self.color],  # if color=1 (black) we look DOWN the board
            [self.location[0] - 1, self.location[1] + 1 - 2 * self.color]
        ]
        neighbors = [board[c] for c in neighbors_coords if 0<=c[0]<board.size and 0<=c[1]<board.size]
        return neighbors_coords, neighbors

    def __nonzero__(self):
        """
        We implement this so that we can do "not Piece" to check if it is a piece or an empty space in the board
        :return:
        """

        return True
