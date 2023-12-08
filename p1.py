from Problem import ProblemClass


def get_sum(line: str, include_words: bool) -> int:
    digits = []
    for i in range(len(line)):
        if line[i].isnumeric():
            digits.append(line[i])
            continue

        if include_words:
            words = {
                'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9
            }
            for word, num in words.items():
                if len(line) >= i + len(word) and line[i:i + len(word)] == word:
                    digits.append(str(num))
                    i = i + len(word)
                    continue

    if digits:
        return int(digits[0] + digits[-1])

    return 0


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        return str(sum([get_sum(line_, include_words=False) for line_ in inp.splitlines()]))

    def _solve(self, inp: str) -> str:
        return str(sum([get_sum(line_, include_words=True) for line_ in inp.splitlines()]))
