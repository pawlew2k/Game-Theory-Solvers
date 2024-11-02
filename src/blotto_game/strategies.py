def strategies(num_units: int, num_bridgeheads: int):  # all units must be deployed
    solution = []

    strategy = [0 for _ in range(num_bridgeheads)]
    strategy[0] = num_units
    solution.append(strategy.copy())

    i = num_bridgeheads - 1
    while i > 0:
        if strategy[i - 1] > strategy[i] + 1:
            strategy[i - 1] -= 1
            strategy[i] += 1
            solution.append(strategy.copy())
            i = min(i + 1, num_bridgeheads - 1)
        else:
            i -= 1

    return solution


def all_strategies(num_units, num_bridgeheads):  # not all units need to be deployed
    solution = []
    for i in range(num_units, -1, -1):
        solution.extend(strategies(i, num_bridgeheads))
    return solution


if __name__ == '__main__':
    num_units = 4
    num_bridgeheads = 3
    print(strategies(num_units, num_bridgeheads))
    print(all_strategies(num_units, num_bridgeheads))
