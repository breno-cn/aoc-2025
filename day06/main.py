from dataclasses import dataclass
import os
import sys
import time
from typing import List

@dataclass
class Problem:
    numbers: List[int]
    operation: str
    
    def solve(self) -> int:
        if self.operation == '+':
            return sum(self.numbers)
        
        result = 1
        for number in self.numbers:
            result *= number

        return result

def read_input() -> List[Problem]:
    with open(os.path.join(sys.path[0], 'input.txt')) as file:
        data = list(map(lambda x: x.strip().split(), file.readlines()))
        
        homework = []
        for i in range(len(data[0])):
            numbers = []
            for j in range(len(data) - 1):
                numbers.append(int(data[j][i]))

            operation = data[-1][i]
            homework.append(Problem(numbers, operation))
            
        return homework

def part1(homework: List[Problem]) -> int:
    return sum(map(Problem.solve, homework))

homework = read_input()

start = time.perf_counter()
result_part_1 = part1(homework)
end = time.perf_counter()
print(f'part 1 took {(end - start):.6f} seconds, result: {result_part_1}')
