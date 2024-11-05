from itertools import permutations
from typing import Tuple


def find_strategies(num_units: int, num_bridgeheads: int) -> list[list[int]]:  # all units must be deployed
    solution = []

    strategy = [0 for _ in range(num_bridgeheads)]
    strategy[0] = num_units
    solution.append(strategy[:])

    pivot = 0
    last = 0
    units_left = 0
    while pivot >= 0:
        if strategy[pivot] > strategy[-1] + 1:
            strategy[pivot] -= 1
            units_left += 1
            while units_left > 0:
                strategy[pivot + 1] = min(strategy[pivot], units_left)
                units_left -= min(strategy[pivot], units_left)
                pivot += 1
            for i in range(pivot + 1, last + 1):
                strategy[i] = 0
            last = pivot
            solution.append(strategy[:])
        else:
            units_left += strategy[pivot]
            pivot -= 1

    return solution


def find_all_strategies(num_units: int, num_bridgeheads: int) -> list[list[int]]:  # not all units need to be deployed
    solution = []
    for i in range(num_units, -1, -1):
        solution.extend(find_strategies(i, num_bridgeheads))
    return solution


def extend_strategies(strategies: list[list[int]], probabilities: list[float]) -> \
        Tuple[list[tuple[int, ...]], list[float]]:
    extended_strategies = []
    extended_probabilities = []
    for strategy, prob in zip(strategies, probabilities):
        permuted_strategies = sorted(list(set(permutations(strategy))), reverse=True)
        num_permutations = len(permuted_strategies)
        extended_strategies.extend(list(permuted_strategies))
        permuted_probabilities = [prob / num_permutations for _ in range(num_permutations)]
        extended_probabilities.extend(permuted_probabilities)
    return extended_strategies, extended_probabilities


def strategies_with_caret(strategies: list[list[int]]) -> str:
    string = '['
    for strategy in strategies:
        if len(set(permutations(strategy))) > 1:
            string += str(strategy)
            string += "^"
        else:
            string += str(tuple(strategy))
        string += ', '
    string = string[:-2] + ']'
    return string


if __name__ == '__main__':
    num_units = 8
    num_bridgeheads = 4

    strategies = find_strategies(num_units, num_bridgeheads)
    extended_strategies, _ = extend_strategies(strategies, [0] * len(strategies))
    all_strategies = find_all_strategies(num_units, num_bridgeheads)
    extended_all_strategies, _ = extend_strategies(all_strategies, [0] * len(all_strategies))

    print(f'Strategies:              {strategies_with_caret(strategies)}',
          f'Extended strategies:     {extended_strategies}',
          f'All strategies:          {strategies_with_caret(all_strategies)}',
          f'Extended all strategies: {extended_all_strategies}', sep='\n')
