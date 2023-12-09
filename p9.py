from __future__ import annotations
from Problem import ProblemClass


def get_next_line(numbers: list[int]) -> list[int]:
    new_numbers = [numbers[i + 1] - numbers[i] for i in range(0, len(numbers) - 1)]
    if all([n == 0 for n in new_numbers]) or len(new_numbers) == 1:
        return []

    return new_numbers


def generate_number_sets(line: str) -> list[list[int]]:
    numbers = [int(n) for n in line.split(' ')]
    number_sets = [numbers]
    while True:
        new_set = get_next_line(number_sets[-1])
        if not new_set:
            break
        number_sets.append(new_set)

    return number_sets


def solve_line(line: str, is_forward: bool = True):
    number_sets = generate_number_sets(line)
    if is_forward:
        while True:
            number_sets[-2].append(number_sets[-2][-1] + number_sets[-1][-1])
            number_sets.pop(-1)
            if len(number_sets) == 1:
                break

        return number_sets[0][-1]

    while True:
        number_sets[-2].insert(0, number_sets[-2][0] - number_sets[-1][0])
        number_sets.pop(-1)
        if len(number_sets) == 1:
            break

    return number_sets[0][0]


class Problem9(ProblemClass):
    def _solve_p1(self, inp: str) -> int:
        lines = inp.splitlines()
        return sum([solve_line(line_) for line_ in lines])

    def _solve(self, inp: str) -> int:
        lines = inp.splitlines()
        return sum([solve_line(line_, is_forward=False) for line_ in lines])
