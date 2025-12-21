from dataclasses import dataclass
import os
import sys
from typing import List
import time

@dataclass
class Ray:
    x: int
    y: int

class World:
    def __init__(self, board: List[List[str]]) -> None:
        self.board: List[List[str]] = board
        self.height: int = len(board)
        self.width: int = len(board[0])
        self.ray_stack = []
        
    def is_finished(self):
        return len(self.ray_stack) == 0

    def is_valid_position(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def try_to_spawn(self, x: int, y: int):
        if not self.is_valid_position(x, y):
            return
        
        if not self.board[y][x] == '.':
            # self.pop_stack()
            return

        self.push_stack(Ray(x, y))
    
    def peek_stack(self) -> Ray:
        return self.ray_stack[-1]
    
    def push_stack(self, ray: Ray):
        self.ray_stack.append(ray)
        
    def pop_stack(self):
        self.ray_stack.pop()

def read_input() -> World:
    with open(os.path.join(sys.path[0], 'input.txt')) as file:
        data = file.readlines()
        return World(list(map(lambda x: list(x.strip()), data)))
    
def part1(world: World) -> int:
    result = 0
    initial_x = world.board[0].index('S')
    initial_y = 1
    world.push_stack(Ray(initial_x, initial_y))
    
    while not world.is_finished():
        current_ray = world.peek_stack()
        x = current_ray.x
        y = current_ray.y

        if not world.is_valid_position(x, y):
            world.pop_stack()
            continue

        if world.board[y][x] == '.':
            world.board[y][x] = '|'
            current_ray.y += 1
            world.pop_stack()
            world.push_stack(current_ray)
            continue
        
        if world.board[y][x] == '|':
            world.pop_stack()
            continue

        if world.board[y][x] == '^':
            #try to spawn left and right
            world.pop_stack()
            world.try_to_spawn(x - 1, y)
            world.try_to_spawn(x + 1, y)
            result += 1
            continue
        
    return result

        
world = read_input()
start = time.perf_counter()
result_part_1 = part1(world)
end = time.perf_counter()

print(f'part 1 took {(end - start):.6f} seconds, result: {result_part_1}')
