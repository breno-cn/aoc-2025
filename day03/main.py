import heapq
import os
import sys
from typing import List

def read_input() -> List[List[int]]:
    filepath = os.path.join(sys.path[0], 'input.txt')
    
    with open(filepath, 'r') as file:
        data = file.readlines()
        return list(map(lambda x: list(map(lambda n: int(n), list(x.strip()))), data))

def highest_joltage(bank: List[int]) -> int:
    highest = heapq.nlargest(1, bank)[0]
    index = bank.index(highest)
    
    if index == len(bank) - 1:
        second_highest = heapq.nlargest(1, bank[:len(bank)-1])[0]
        return second_highest*10 + highest

    second_highest = heapq.nlargest(1, bank[index+1:])[0]
    return highest*10 + second_highest

def part1(batteries: List[List[int]]) -> int:
    return sum(map(highest_joltage, batteries))

batteries = read_input()

result_part_1 = part1(batteries)
print(result_part_1)