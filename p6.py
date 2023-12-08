import math
from Problem import ProblemClass


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        times = inp.splitlines()[0]
        distances = inp.splitlines()[1]

        times = [int(t) for t in times.split(':')[1].split(' ') if t]
        distances = [int(d) for d in distances.split(':')[1].split(' ') if d]

        multiplier = 1
        for i in range(len(times)):
            multiplier *= self.solve_one(times[i], distances[i])

        return str(multiplier)

    def _solve(self, inp: str) -> str:
        times = inp.splitlines()[0]
        distances = inp.splitlines()[1]
        record = int(times.split(':')[1].replace(' ', ''))
        distance = int(distances.split(':')[1].replace(' ', ''))

        return str(self.solve_one(record, distance))

    def solve_one(self, record: int, distance: int) -> int:
        lower = abs(-record + math.sqrt(record * record - 4 * 1 * distance)) / 2 + 0.001
        upper = abs(-record - math.sqrt(record * record - 4 * 1 * distance)) / 2 - 0.001
        return int(math.floor(upper) - math.ceil(lower) + 1)
