class Rover(object):
    """
    The Rover 'state object' representing the rovers position and orientation on Mars' surface.
    Exposes methods to turn and move the rover, as well as to query its position.
    """

    allowed_orientations = ['N', 'S', 'E', 'W']

    def __init__(self, x = 0, y = 0, orientation = 'N', width = 5, height = 5):
        if not orientation.upper() in Rover.allowed_orientations:
            raise ValueError(
                    'Illegal orientation: {}. Allowed are {}'
                    .format(orientation, Rover.allowed_orientations)
                    )
        if not (x >= 0 and y >= 0):
            raise ValueError('x and y coordinates must not be smaller than 0!')
        if not (width >= 0 and height >= 0):
            raise ValueError('width and height must not be smaller than 0')
        if x > width or y > height:
            raise ValueError('x and y coordinates must not be greter than height or width, respectively')

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

