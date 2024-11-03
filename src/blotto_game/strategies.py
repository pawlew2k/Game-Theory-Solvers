from itertools import permutations


def find_strategies(num_units: int, num_bridgeheads: int):  # all units must be deployed
    solution = []

    strategy = [0 for _ in range(num_bridgeheads)]
    strategy[0] = num_units
    solution.append(strategy.copy())

    from_pivot = 0
    to_pivot = 1
    while from_pivot >= 0 and to_pivot < num_bridgeheads:
        difference = strategy[from_pivot] - strategy[to_pivot]
        if difference > 1:
            strategy[from_pivot] -= 1
            strategy[to_pivot] += 1
            solution.append(strategy.copy())
            to_pivot = min(to_pivot + 1, num_bridgeheads - 1)
            from_pivot = to_pivot - 1
        elif difference == 1:
            from_pivot -= 1
        else:
            from_pivot -= 1
            to_pivot -= 1

    return solution


def find_all_strategies(num_units, num_bridgeheads):  # not all units need to be deployed
    solution = []
    for i in range(num_units, -1, -1):
        solution.extend(find_strategies(i, num_bridgeheads))
    return solution


def extend_strategies(strategies, probabilities):
    extended_strategies = []
    extended_probabilities = []
    for strategy, prob in zip(strategies, probabilities):
        permuted_strategies = sorted(list(set(permutations(strategy))), reverse=True)
        num_permutations = len(permuted_strategies)
        extended_strategies.extend(list(permuted_strategies))
        permuted_probabilities = [prob / num_permutations for _ in range(num_permutations)]
        extended_probabilities.extend(permuted_probabilities)
    return extended_strategies, extended_probabilities


def strategies_with_caret(strategies):
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
    num_units = 4
    num_bridgeheads = 3

    strategies = find_strategies(num_units, num_bridgeheads)
    extended_strategies, _ = extend_strategies(strategies, [0] * len(strategies))
    all_strategies = find_all_strategies(num_units, num_bridgeheads)
    extended_all_strategies, _ = extend_strategies(all_strategies, [0] * len(all_strategies))

    print(f'Strategies:              {strategies_with_caret(strategies)}',
          f'Extended strategies:     {extended_strategies}',
          f'All strategies:          {strategies_with_caret(all_strategies)}',
          f'Extended all strategies: {extended_all_strategies}', sep='\n')
