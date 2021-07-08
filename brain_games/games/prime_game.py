from random import randint

from brain_games.main_game import game


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    exp_ans = True
    count = 0
    que = []
    ans = []
    while count < 3:
        count += 1
        num = randint(2, 100)
        que.append(num)
        if num == 2:
            ans.append('yes')
            continue
        elif num % 2 == 0:
            ans.append('no')
            continue
        for index in range(3, num):
            if num % index == 0:
                ans.append('no')
                break
            ans.append('yes')
            break
    game(task, que, ans, exp_ans)
