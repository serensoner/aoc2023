from functools import reduce
from Problem import ProblemClass


def parse_line(line_: str) -> dict:
    line_id = int(line_.split(' ')[1][:-1])
    sets = line_.split(':')[1]
    subsets = sets.split(';')
    return_parts = []
    for subset in subsets:
        parts = subset.split(',')
        for part in parts:
            part = part.strip()
            count = int(part.split(' ')[0])
            color = part.split(' ')[1]
            return_parts.append({'color': color, 'count': count})

    return {'line_id': line_id, 'parts': return_parts}


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        max_counts = {'red': 12, 'green': 13, 'blue': 14}
        possibles = []

        for line in inp.splitlines():
            line_details = parse_line(line)
            if all([p['count'] <= max_counts[p['color']] for p in line_details['parts']]):
                possibles.append(line_details['line_id'])

        return sum(possibles)

    def _solve(self, inp: str) -> str:
        powers = []

        for line in inp.splitlines():
            line_details = parse_line(line)
            mins = {
                color: max([p['count'] for p in line_details['parts'] if p['color'] == color])
                for color in ['red', 'green', 'blue']
            }

            power = reduce((lambda x, y: x * y), mins.values())
            powers.append(power)

        return sum(powers)
