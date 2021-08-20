from random import randint

from brain_games.main_game import game


def brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    ans = []
    que = [f'{randint(1, 100)} {randint(1, 100)}' for _ in range(3)]
    for q in que:
        maximum = int(max(q.split(' ')))
        minimum = int(min(q.split(' ')))
        mod = maximum % minimum
        while mod != 0:
            maximum = minimum
            minimum = mod
            mod = maximum % minimum
        ans.append(str(minimum))
    game(task, que, ans, True)
