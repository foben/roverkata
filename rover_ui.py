#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
from rover import Rover

orient = {
        'N': '^',
        'S': 'v',
        'E': '>',
        'W': '<'
    }

cmd_mapping = {
        'R': lambda r: r.right(),
        'L': lambda r: r.left(),
        'F': lambda r: r.forward(),
        'B': lambda r: r.backward(),
    }

def main():
    rover = new_game()
    print_board(rover)
    
    while True:
        input = stdin.readline().strip()
        if input.upper() == 'EXIT':
            print 'bye bye!'
            break
        elif input.upper() == 'NEW':
            rover = new_game()
        else:
            print 'parsing'
            rover = parse_and_apply(input, rover)
        print_board(rover)

def parse_and_apply(input, rover):
    for s in [s.upper() for s in input.split(",")]:
        if s in cmd_mapping:
            rover = cmd_mapping[s](rover)
        else:
            print 'Unrecognised command: {}'.format(s)
        
    return rover

def print_board(rover):
    rover_x = rover.get_position()[0]
    rover_y = rover.get_position()[1]
    default_line = ''.join(['·' for w in range(rover.get_width())])
    current_line = ['·' for w in range(rover.get_width())]
    current_line[rover_x] = orient[rover.get_orientation()] 
    current_line = ''.join(current_line) 
    for h in range(rover.get_height()):
        if rover_y != h:
            print default_line
        else:
            print current_line

def new_game():
    print 'Please specify desired width: '
    width = read_int()
    print 'Please specify desired height: '
    height = read_int()
    print 'Please specify desired horizontal starting position: '
    x = read_int()
    print 'Please specify desired vertical starting position: '
    y = read_int()
    return Rover(x = x, y = y, width = width, height = height)

def read_int():
    try:
        return int(stdin.readline())
    except Exception:
        print 'Not a valid number, please try again:'
        return read_int()

if __name__ == '__main__':
    main()
