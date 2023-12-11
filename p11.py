import itertools
from Problem import ProblemClass


def get_positions(lines) -> list[tuple]:
    positions = []
    for j in range(len(lines)):
        line = lines[j]
        for i in range(len(line)):
            if line[i] == '#':
                positions.append((j, i))

    return positions


def get_sum_dist(inp: str, coeff: int):
    lines = inp.splitlines()
    positions = get_positions(lines)
    empty_rows = [i for i in range(len(lines)) if i not in [p[0] for p in positions]]
    empty_columns = [j for j in range(len(lines[0])) if j not in [p[1] for p in positions]]

    return sum([
        abs(pos1[1] - pos0[1]) + abs(pos1[0] - pos0[0]) + \
        coeff * len([e for e in empty_rows if min(pos0[0], pos1[0]) < e < max(pos0[0], pos1[0])]) + \
        coeff * len([e for e in empty_columns if min(pos0[1], pos1[1]) < e < max(pos0[1], pos1[1])])
        for pos0, pos1 in itertools.combinations(positions, 2)
    ])


class Problem11(ProblemClass):
    def _solve_p1(self, inp: str) -> int:
        return get_sum_dist(inp, 1)

    def _solve(self, inp: str) -> int:
        return get_sum_dist(inp, 1_000_000 - 1)
