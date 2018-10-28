#! /usr/bin/env python2


def robot_move(moves):
    moves = [('N', 2), ('E',4), ('S', 1), ('W', 3)]
    x = 0
    y = 0

    for move in moves:
        if move[0] == "N":
            y = y + move[1]
        if move[0] == "S":
            y = y - move[1]
        if move[0] == "E":
            x = x + move[1]
        if move[0] == "W":
            x = x - move[1]
    return(x, y)
