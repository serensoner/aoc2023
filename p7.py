import math
from dataclasses import dataclass, field
from Problem import ProblemClass


@dataclass(order=True)
class Hand:
    cards: list[str]
    bid: int
    include_js: bool
    strength: int = None
    rank: int = None
    sort_index: int = field(init=False)

    def __post_init__(self):
        self.bid = int(self.bid)
        counts = {c: self.cards.count(c) for c in self.cards}
        j_count = counts.pop('J', 0) if self.include_js else 0
        counts = list(counts.values())

        counts.sort(reverse=True)
        if len(counts) == 0:
            self.strength = 7
        elif counts[0] + j_count == 5:
            self.strength = 7
        elif counts[0] + j_count == 4:
            self.strength = 6
        elif counts[0] + j_count == 3 and counts[1] == 2:
            self.strength = 5
        elif counts[0] + j_count == 3 and counts[1] == 1:
            self.strength = 4
        elif counts[0] + j_count == 2 and len(counts) == 3:
            self.strength = 3
        elif counts[0] + j_count == 2 and len(counts) == 4:
            self.strength = 2
        else:
            self.strength = 1

        def char_to_val(c) -> str:
            match c:
                case 'A': return '14'
                case 'K': return '13'
                case 'Q': return '12'
                case 'J': return '01'
                case 'T': return '10'
                case _: pass

            return f'0{c}'

        self.sort_index = int(f'''{self.strength}{''.join([char_to_val(c) for c in self.cards])}''')


def parse_hands(inp: str, include_js: bool) -> list[Hand]:
    lines = inp.splitlines()
    hands = []
    for line in lines:
        chars, bid = line.split(' ')
        hands.append(Hand(chars, bid, include_js))

    hands.sort(key=lambda x: x.sort_index)
    return hands


def calculate_winnings(hands: list[Hand]) -> int:
    winnings = sum([(1 + rank) * hand.bid for rank, hand in enumerate(hands)])
    return winnings


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        hands = parse_hands(inp, False)
        return calculate_winnings(hands)

    def _solve(self, inp: str) -> str:
        hands = parse_hands(inp, True)
        return calculate_winnings(hands)

