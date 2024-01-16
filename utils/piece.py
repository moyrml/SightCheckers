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
        :return: dict. Dictionary with end positions as keys and captured positions as values
        """
        captured_positions = dict()

        neighbors_1st_order_coords, neighbors_1st_order = self.get_forward_neighbors(board)
        for i, n1 in enumerate(neighbors_1st_order):
            if not n1 or n1.color == self.color:
                # First neighboring position is empty
                continue

            neighbors_2st_order_coords, neighbors_2st_order = n1.get_forward_neighbors(board, color_mod=self.color)
            for j, n2 in enumerate(neighbors_2st_order):
                if not n2:
                    # Second neighboring position is empty
                    if neighbors_2st_order_coords[j][0] - self.location[0] not in [-2, 2]:
                        # direction consistancy
                        continue
                    captured_positions[tuple(neighbors_2st_order_coords[j])] = n1.location

        return captured_positions

    def get_forward_neighbors(self, board, color_mod=None):
        """

        :param board:
        :param color_mod: int. One of board.colors. Used to determine second order neighbors.
        :return:
        """
        forward_locations = self.get_forward_location(board.size, color_mod)
        neighbors = [board[c] for c in forward_locations]

        return forward_locations, neighbors

    def get_forward_location(self, board_size, color_mod=None):
        """
        Helper function to get the legal forward locations
        :return: list of tuples
        """
        color = self.color
        if color_mod is not None:
            color = color_mod

        xs = self.location[0] + 1, self.location[0] - 1
        ys = self.location[1] + 1 - 2 * color,

        out = [(x, y) for x in xs for y in ys if 0<=x<board_size and 0<=y<board_size]
        return out

    def __nonzero__(self):
        """
        We implement this so that we can do "not Piece" to check if it is a piece or an empty space in the board
        :return:
        """

        return True
