import math
from enum import Enum

Direction = Enum('Direction', ['right', 'down', 'left', 'up'])

def set_next_number(x,y,dir,number, field):
    match dir:
        case Direction.right:
            x += 1
        case Direction.down:
            y += 1
        case Direction.left:
            x -= 1
        case Direction.up:
            y -= 1
    field[y][x] = number
    return x,y,field

def update_direction(x,y,dir,field):
    match dir:
        case Direction.right:
            if field[y+1][x] == -1:
                return Direction.down
        case Direction.down:
            if field[y][x-1] == -1:
                return Direction.left
        case Direction.left:
            if field[y-1][x] == -1:
                return Direction.up
        case Direction.up:
            if field[y][x+1] == -1:
                return Direction.right
    return dir

input = 13
digits = len(str(input))

side = math.ceil(math.sqrt(input))

output = [[-1 for x in range(side)] for y in range(side)] 

center = math.ceil(side/2) - 1

x = y = center
current_number = 0

output[y][x] = current_number
current_number += 1

direction = Direction.right

while (current_number < input):
    x,y,output = set_next_number(x,y,direction,current_number,output)
    direction = update_direction(x,y,direction,output)
    current_number += 1

for line in output:
    if any(i >= 0 for i in line):
        print(' '.join([' ' * digits if n == -1 else str(n).rjust(digits) for n in line]))
