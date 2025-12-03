import os
import sys
from typing import List

import time

def read_input() -> List[tuple[int, int]]:
    filepath = os.path.join(sys.path[0], 'input.txt')
    
    with open(filepath, 'r') as file:
        data = file.read().split(',')
        ranges = map(lambda x: x.split('-'), data)
        
        return list(map(lambda x: (int(x[0]), int(x[1])), ranges))

def is_valid_id(id: int) -> bool:
    number_size = len(str(id))
    n = number_size // 2
    first_half = str(id)[0:n]
    second_half = str(id)[n:]
    
    return first_half != second_half


def part1(ranges: List[tuple[int, int]]):
    result = 0

    for ids in ranges:
        begin = ids[0]
        end = ids[1]

        for id in range(begin, end + 1):
            if not is_valid_id(id):
                # print(f'id not valid: {id}')
                result += id

    return result

def generate_windows(array: str, size: int) -> List[List[int]]:
    result = []
    left = 0
    right = size
    
    while right <= len(array):
        result.append(array[left:right])
        left += size
        right += size

    if left < len(array):
        result.append(array[left:])
        
    return result

def all_equal(arr: List[str]) -> bool:
    for i in arr[1:]:
        if i != arr[0]:
            return False

    return True

def is_valid_id_part2(id: int) -> bool:
    number = str(id)
    number_size = len(number)
    window_size = 1

    while window_size <= number_size // 2:
        windows = generate_windows(number, window_size)
        if all_equal(windows):
            #print(windows)
            return False
        # if len(windows) != len(set(windows)):
            # print(windows)
            # return False
        # print(windows)
        #print(f'windows for id {id} -> {windows}')
        #if all(x == windows[0] for x in windows):
        #    return False

        window_size += 1
        
    return True

def part2(ranges: List[tuple[int, int]]):
    result = 0
    
    for ids in ranges:
        begin = ids[0]
        end = ids[1]
        
        for id in range(begin, end + 1):
            if not is_valid_id_part2(id):
                #print(f'id not valid: {id}') 
                result += id
                # break
                
    return result

        
ranges = read_input()

start = time.perf_counter()
result_part_1 = part1(ranges)
end = time.perf_counter()

print(f'part 1 took {(end - start):.6f} seconds, result: {result_part_1}')

start = time.perf_counter()
result_part_2 = part2(ranges)
end = time.perf_counter()

print(f'part 2 took {(end - start):.6f} seconds, result: {result_part_2}')

#print(generate_windows('1010', 2))