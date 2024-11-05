from typing import Tuple

import numpy as np
from scipy.optimize import linprog


def solve_payoff_table(A: np.array) -> Tuple[int, list[float], list[float]]:
    game_value, second_player_strategy = solve(A)
    _, first_player_strategy = solve(-A.T)
    return game_value, first_player_strategy, second_player_strategy


def solve(A: np.array) -> Tuple[int, list[float]]:
    m, n = np.shape(A)
    c = np.concatenate((np.zeros(n), [1]))
    b_ub = np.zeros(m)
    A_ub = np.concatenate((A, np.full(shape=(m, 1), fill_value=-1)), axis=1)
    sum_is_one = np.concatenate((np.ones(n), [0])).reshape(1, -1)
    bounds = [[0, None] for _ in range(n)] + [[None, None]]
    result = linprog(c, A_ub, b_ub, A_eq=sum_is_one, b_eq=[1], bounds=bounds, method='highs')
    game_value = result.fun
    second_player_strategy = result.x[:-1].tolist()
    return game_value, second_player_strategy


if __name__ == '__main__':
    v, X, Y = solve_payoff_table(
        # np.array(
        #     [[1, -1, 2],
        #      [-1, 2, 0],
        #      [1, 0, -1]]
        # )
        np.array(
            [[1/2, 0],
             [1, 1/2],
             [1, 3/2],
             [1, 2]]
        )
    )

    print(f'Value of the game: {v}',
          f'Optimal strategy of the first player: {X}',
          f'Optimal strategy of the second player: {Y}', sep='\n')
