from random import randint

from brain_games.main_game import game


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    exp_ans = True
    ans = []
    que = [randint(2, 100) for _ in range(3)]
    for num in que:
        if num % 2 == 0 and num != 2 or num % 3 == 0:
            ans.append('no')
            continue
        ans.append('yes')
        continue
    game(task, que, ans, exp_ans)
