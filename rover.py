#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Rover(object):
    """
    The Rover 'state object' representing the rovers position and orientation on Mars' surface.
    Exposes methods to turn and move the rover, as well as to query its position.
    """

    allowed_orientations = ['N', 'E', 'S', 'W']
    __movements = { 
            'N' : [0, -1],
            'E' : [1, 0],
            'S' : [0, 1],
            'W' : [-1, 0]
        }

    def __init__(self, x = 0, y = 0, orientation = 'N', width = 5, height = 5):
        if not orientation.upper() in Rover.allowed_orientations:
            raise ValueError(
                    'Illegal orientation: {}. Allowed are {}'
                    .format(orientation, Rover.allowed_orientations)
                    )
        if not (x >= 0 and y >= 0):
            raise ValueError('x and y coordinates must not be smaller than 0!')
        if not (width > 0 and height > 0):
            raise ValueError('width and height must be greater than 0')
        if x >= width or y >= height:
            raise ValueError('coordinate-indices ({}, {}) are out of range for the dimensions ({} x {})'
                    .format(x, y, width, height))

        self.x = x
        self.y = y
        self.orientation = orientation.upper()
        self.width = width
        self.height = height

    def forward(self):
        to_move = Rover.__movements[self.orientation]
        return self.__do_move(to_move)

    def backward(self):
        to_move = [-1 * x for x in Rover.__movements[self.orientation]]
        return self.__do_move(to_move)

    def __do_move(self, to_move):
        newpos = [ a + b for (a,b) in zip(to_move, [self.x, self.y])] 
        new_x = newpos[0] % self.width
        new_y = newpos[1] % self.height
        return Rover(new_x, new_y, self.orientation, self.width, self.height)

    def left(self):
        return self.__do_turn(-1)

    def right(self):
        return self.__do_turn(1)

    def __do_turn(self, amount):
        orientation_index = Rover.allowed_orientations.index(self.orientation)
        new_orientation_index = (orientation_index + amount) % len(Rover.allowed_orientations)
        new_orientation = Rover.allowed_orientations[new_orientation_index]
        return Rover(self.x, self.y, new_orientation, self.width, self.height)

    def get_position(self):
        return (self.x, self.y)

    def get_orientation(self):
        return self.orientation

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

