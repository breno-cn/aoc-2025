from math import floor
import os
import sys
from typing import List

def read_input() -> List[str]:
    filepath = os.path.join(sys.path[0], 'input.txt')
    
    with open(filepath, 'r') as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def move(direction: str, steps: int, current_position: int) -> int:
    if direction == 'R':
        return (current_position + steps) % 100
    
    return (current_position - steps) % 100 

def move2(direction: str, steps: int, current_position: int) -> tuple[int, int]:
    if direction == 'R':
        next_position = (current_position + steps) % 100
        passes = steps // 100
        if (current_position != 0 and next_position < current_position) or next_position == 0:
            passes += 1
        
        print(f'movement: {direction}{steps} -> current: {current_position} next: {next_position} passes {passes}')
        return next_position, passes

    next_position = (current_position - steps) % 100
    passes = steps // 100
    if (current_position != 0 and next_position > current_position) or next_position == 0:
        passes += 1
    
    print(f'movement: {direction}{steps} -> current: {current_position} next: {next_position} passes {passes}')
    return next_position, floor(passes)
    

def part1(movements: List[str]) -> int:
    current_position = 50
    password = 0

    for movement in movements:
        direction = movement[0]
        steps = int(movement[1:])
        current_position = move(direction, steps, current_position)

        if current_position == 0:
            password += 1

    return password

def part2(movements: List[str]) -> int:
    current_position = 50
    password = 0

    for movement in movements:
        direction = movement[0]
        steps = int(movement[1:])
        current_position, passes = move2(direction, steps, current_position)
        
        password += passes

    return password


movements = read_input()
result_part_1 = part1(movements)
result_part_2 = part2(movements)

print(result_part_1)
print(result_part_2)
