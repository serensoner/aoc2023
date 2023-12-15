import itertools
import re
from collections import OrderedDict

from Problem import ProblemClass


def get_hash(part: str) -> int:
    hash_val = 0
    for c in part:
        hash_val = (hash_val + ord(c)) * 17 % 256
    return hash_val


class Problem15 (ProblemClass):
    def _solve_p1(self, inp: str) -> int:
        return sum([get_hash(part) for part in inp.split(',')])

    def _solve(self, inp: str) -> int:
        boxes = {i: OrderedDict() for i in range(256)}
        for part in inp.split(','):
            parts = re.findall('([a-z]*)([\=,\-])*(\d)*', part)[0]
            label = parts[0]
            box_nr = get_hash(label)
            sign = parts[1]
            if '=' in sign:
                num = int(parts[2])
                boxes[box_nr][label] = num
            elif '-' in sign and label in boxes[box_nr]:
                del boxes[box_nr][label]

        return sum([
            (box_nr + 1) * (i + 1) * v
            for box_nr, contents in boxes.items()
            for i, v in enumerate(contents.values())
        ])
