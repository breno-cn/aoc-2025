import os
import sys
from typing import List

def read_input() -> List[List[str]]:
    with open(os.path.join(sys.path[0], 'input.txt')) as file:
        return list(map(lambda x: list(x.strip()), file.readlines()))

def is_valid_position(board: List[List[str]], i: int, j: int) -> bool:
    return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

def is_position_reachable(board: List[List[str]], i: int, j: int) -> bool:
    total = 0

    for new_i in range(i - 1, i + 2):
        for new_j in range(j - 1, j + 2):
            if not is_valid_position(board, new_i, new_j):
                continue

            if new_i == i and new_j == j:
                continue
            
            if board[new_i][new_j] == '@':
                total += 1

    return total < 4
            
def part1(board: List[List[str]]) -> int:
    result = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                continue

            if is_position_reachable(board, i, j):
                result += 1

    return result

def part2(board: List[List[str]]) -> int:
    result = 0

    while True:
        removedPaper = False
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue

                if is_position_reachable(board, i, j):
                    board[i][j] = '.'
                    result += 1
                    removedPaper = True
        
        if not removedPaper:
            break

    return result

    
board = read_input()
result_part_1 = part1(board)
print(result_part_1)

result_part_2 = part2(board)
print(result_part_2)
