from random import randint

from brain_games.main_game import game


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    exp_ans = True
    ans = []
    que = [randint(2, 100) for _ in range(3)]
    for num in que:
        if is_prime(num):
            ans.append('yes')
            continue
        ans.append('no')
    game(task, que, ans, exp_ans)


def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for index in range(3, num):
        if num % index == 0:
            return False
    return True
