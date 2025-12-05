from dataclasses import dataclass
import os
import sys
import time
from typing import List


def read_input() -> tuple[List[tuple[int, int]], List[int]]:
    with open(os.path.join(sys.path[0], 'input.txt')) as file:
        data = file.read().split('\n\n')

        fresh_ranges = []
        for range in data[0].split('\n'):
            # print(range)
            clean_range = range.strip().split('-')
            fresh_ranges.append((int(clean_range[0]), int(clean_range[1])))
        
        ingredients = list(map(lambda x: int(x.strip()), data[1].split('\n')))
        
        return fresh_ranges, ingredients
    
def ingredient_is_fresh(ingredient: int, fresh_ranges: List[tuple[int, int]]) -> bool:
    for range in fresh_ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True

    return False
    
def part1(fresh_ranges: List[tuple[int, int]], ingredients: List[int]) -> int:
    result = 0

    for ingredient in ingredients:
        if ingredient_is_fresh(ingredient, fresh_ranges):
            # print(ingredient)
            result += 1

    return result

fresh_ranges, ingredients = read_input()    
#print(fresh_ranges, ingredients)

result_part_1 = part1(fresh_ranges, ingredients)
print(result_part_1)
