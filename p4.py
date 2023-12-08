import math
from Problem import ProblemClass


def get_winning_count(line_: str) -> int:
    cards = line_.split(':')
    parts = cards[1].split(' | ')
    winning_numbers = [int(w.strip()) for w in parts[0].split(' ') if w.strip()]
    my_numbers = [int(w.strip()) for w in parts[1].split(' ') if w.strip()]
    return len([w for w in winning_numbers if w in my_numbers])


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        return sum([int(math.pow(2, get_winning_count(line) - 1)) for line in inp.splitlines()])

    def _solve(self, inp: str) -> str:
        scores = [get_winning_count(line) for line in inp.splitlines()]

        counts = [1] * len(scores)
        for i in range(len(scores)):
            for j in range(scores[i]):
                counts[j + i + 1] += (counts[i])

        return sum(counts)
