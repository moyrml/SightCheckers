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
