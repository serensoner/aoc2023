from __future__ import annotations
import math
from Problem import ProblemClass


class Problem(ProblemClass):
    def _solve_p1(self, inp: str) -> str:
        lines = inp.splitlines()
        instructions = lines[0]

        map = {}

        for line in lines[2:]:
            node_name = line[0:3]
            left = line[7:10]
            right = line[12:15]
            map[node_name] = {'L': left, 'R': right}

        current_node = 'AAA'
        inst_id = 0
        while current_node != 'ZZZ':
            current_node = map[current_node][instructions[inst_id % len(instructions)]]
            inst_id += 1

        return str(inst_id)

    def _solve(self, inp: str) -> str:
        lines = inp.splitlines()
        instructions = lines[0]

        network = {}

        for line in lines[2:]:
            node_name = line[0:3]
            left = line[7:10]
            right = line[12:15]
            network[node_name] = {'L': left, 'R': right, 'Z_dist': 1E6}

        starting_nodes = [n for n in network.keys() if n.endswith('A')]
        current_nodes = starting_nodes
        inst_id = 0
        while not all(c.endswith('Z') for c in current_nodes):
            current_nodes = [network[c][instructions[inst_id % len(instructions)]] for c in current_nodes]
            inst_id += 1
            for i, c in enumerate(current_nodes):
                if c.endswith('Z'):
                    current_dist = network[starting_nodes[i]]['Z_dist']
                    network[starting_nodes[i]]['Z_dist'] = min(inst_id, current_dist)

            if all([network[starting_node]['Z_dist'] < 1E6 for starting_node in starting_nodes]):
                break

        lcm = math.lcm(*[network[starting_node]['Z_dist'] for starting_node in starting_nodes])
        return str(lcm)
