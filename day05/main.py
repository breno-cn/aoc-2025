from dataclasses import dataclass
import os
import sys
import time
from typing import List

@dataclass
class Range:
    start: int
    end: int

def read_input() -> tuple[List[Range], List[int]]:
    with open(os.path.join(sys.path[0], 'input.txt')) as file:
        data = file.read().split('\n\n')

        fresh_ranges = []
        for range in data[0].split('\n'):
            clean_range = range.strip().split('-')
            fresh_ranges.append(Range(int(clean_range[0]), int(clean_range[1])))
        
        ingredients = list(map(lambda x: int(x.strip()), data[1].split('\n')))
        
        return fresh_ranges, ingredients
    
def ingredient_is_fresh(ingredient: int, fresh_ranges: List[Range]) -> bool:
    for range in fresh_ranges:
        if ingredient >= range.start and ingredient <= range.end:
            return True

    return False
    
def part1(fresh_ranges: List[Range], ingredients: List[int]) -> int:
    result = 0

    for ingredient in ingredients:
        if ingredient_is_fresh(ingredient, fresh_ranges):
            result += 1

    return result

def can_be_merged(a: Range, b: Range) -> bool:
    return a.start <= b.end and b.start <= a.end

def merge(a: Range, b: Range) -> Range:
    return Range(min(a.start, b.start), max(a.end, b.end))

def part2(fresh_ranges: List[Range]) -> int:
    result = 0
    fresh_ranges.sort(key=lambda x: x.start)

    current_range = fresh_ranges[0]
    for range in fresh_ranges[1:]:
        if can_be_merged(current_range, range):
            current_range = merge(current_range, range)
        else:
            result += current_range.end - current_range.start + 1
            current_range = range

    result += current_range.end - current_range.start + 1
    return result

fresh_ranges, ingredients = read_input()    

start = time.perf_counter()
result_part_1 = part1(fresh_ranges, ingredients)
end = time.perf_counter()
print(f'part 1 took {(end - start):.6f} seconds, result: {result_part_1}')

start = time.perf_counter()
result_part_2 = part2(fresh_ranges)
end = time.perf_counter()
print(f'part 2 took {(end - start):.6f} seconds, result: {result_part_2}')
