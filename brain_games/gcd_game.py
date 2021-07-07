from random import randint

from brain_games.main_game import game


def brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    count = 0
    que = []
    ans = []
    while count < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        que.append('{ar1} {ar2}'.format(ar1=num1, ar2=num2))
        if num1 < num2:
            maximum = num2
            minimum = num1
        else:
            maximum = num1
            minimum = num2
        mod = maximum % minimum
        if mod == 0:
            ans.append(str(minimum))
            count += 1
        else:
            while mod != 0:
                maximum = minimum
                minimum = mod
                mod = maximum % minimum
            ans.append(str(minimum))
            count += 1
    game(task, que, ans)
