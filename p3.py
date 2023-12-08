import re
from Problem import ProblemClass


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        input_lines = inp.splitlines()

        non_symbols = [str(c) for c in range(10)] + ['.']
        numbers = []

        for line_num, line in enumerate(input_lines):
            words = [a.group() for a in re.finditer('(\d)*\w+', line)]
            last_pos = -1
            for word in words:
                if word.isnumeric():
                    start = line.find(word, last_pos + 1)
                    end = start + len(word)
                    last_pos = end
                    if line_num + 1 < len(input_lines):
                        for x in range(max(0, start - 1), min(end + 1, len(line) - 1)):
                            if input_lines[line_num + 1][x] not in non_symbols:
                                numbers.append(int(word))
                                break
                    if line_num - 1 >= 0:
                        for x in range(max(0, start - 1), min(end + 1, len(line) - 1)):
                            if input_lines[line_num - 1][x] not in non_symbols:
                                numbers.append(int(word))
                                break
                    if end + 1 < len(line):
                        if input_lines[line_num][end] not in non_symbols:
                            numbers.append(int(word))
                            break
                    if start - 1 >= 0:
                        if input_lines[line_num][start - 1] not in non_symbols:
                            numbers.append(int(word))
                            break

        return sum(numbers)

    def _solve(self, inp: str) -> str:
        gears = {}

        input_lines = inp.splitlines()

        def add_gear(x, y, num):
            if (x, y) in gears:
                gears[(x, y)].append(num)
            else:
                gears[(x, y)] = [num]

        for line_num, line in enumerate(input_lines):
            words = [a.group() for a in re.finditer('(\d)*\w+', line)]
            last_pos = -1
            for word in words:
                if word.isnumeric():
                    start = line.find(word, last_pos + 1)
                    end = start + len(word)
                    last_pos = end
                    if line_num + 1 < len(input_lines):
                        for x in range(max(0, start - 1), min(end + 1, len(line) - 1)):
                            if input_lines[line_num + 1][x] == '*':
                                add_gear(x, line_num + 1, int(word))
                    if line_num - 1 >= 0:
                        for x in range(max(0, start - 1), min(end + 1, len(line) - 1)):
                            if input_lines[line_num - 1][x] == '*':
                                add_gear(x, line_num - 1, int(word))
                    if end + 1 < len(line):
                        if input_lines[line_num][end] == '*':
                            add_gear(end, line_num, int(word))
                    if start - 1 >= 0:
                        if input_lines[line_num][start - 1] == '*':
                            add_gear(start - 1, line_num, int(word))

        return sum([
            nl[0] * nl[1] for nl in gears.values() if len(nl) == 2
        ])
