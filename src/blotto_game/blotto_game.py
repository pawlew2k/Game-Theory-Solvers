from itertools import permutations
from math import factorial
import numpy as np

from strategies import strategies
from src.payoff_table_solver import solve_payoff_table


def blotto_game(strategies1, strategies2, score_for_killed=True):
    arr = np.zeros((len(strategies1), len(strategies2)))
    for idx1, strategy1 in enumerate(strategies1):
        for idx2, strategy2 in enumerate(strategies2):
            score = 0
            for split1 in permutations(strategy1):
                for split2 in permutations(strategy2):
                    bridgeheads = zip(split1, split2)
                    for unit1, unit2 in bridgeheads:
                        unit1, unit2 = int(unit1), int(unit2)

                        if unit1 > unit2:
                            score += 1
                            if score_for_killed:
                                score += unit2
                        if unit2 > unit1:
                            score -= 1
                            if score_for_killed:
                                score -= unit1

            score /= factorial(len(strategies1[0])) * factorial(len(strategies2[0]))
            arr[idx1, idx2] = float(score)
    return arr


if __name__ == '__main__':
    num_bridgeheads = 2
    strategiesB = strategies(6, num_bridgeheads)
    strategiesK = strategies(4, num_bridgeheads)
    A = blotto_game(strategiesB, strategiesK, score_for_killed=False)
    v, x, y = solve_payoff_table(A)

    print(f'{strategiesB=}')
    print(f'{strategiesK=}')
    print(f'A=\n{A}')
    print(f'{v=}')
    print(f'{x=}')
    print(f'{y=}')


