from random import randint, choice

from brain_games.main_game import game


def brain_calc():
    task = 'What is the result of the expression?'
    count = 0
    que = []
    ans = []
    while count < 3:
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        sign = choice(('+', '-', '*'))
        que.append('{ar1} {ar2} {ar3}'.format(ar1=num1, ar2=sign, ar3=num2))
        count += 1
        if sign == '+':
            ans.append(str(num1 + num2))
        elif sign == '-':
            ans.append(str(num1 - num2))
        elif sign == '*':
            ans.append(str(num1 * num2))
    game(task, que, ans)
