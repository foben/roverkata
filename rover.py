class Rover(object):
    """
    The Rover 'state object' representing the rovers position and orientation on Mars' surface.
    Exposes methods to turn and move the rover, as well as to query its position.
    """

    def __init__(self, x = 0, y = 0, orientation = 'N', width = 5, height = 5):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.width = width
        self.height = height

    def forward(self):
        pass

    def backward(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def get_position(self):
        return (self.x, self.y)

    def get_orientation(self):
        return self.orientation

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

