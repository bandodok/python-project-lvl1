from random import randint

from brain_games.main_game import game


def brain_progression():
    task = 'What number is missing in the progression?'
    exp_ans = True
    count = 0
    que = []
    ans = []
    min_len = 5
    max_len = 15
    while count < 3:
        start = randint(0, 100)
        step = randint(1, 5)
        end = randint(min_len, max_len) * step + start
        progression = list(range(start, end, step))
        index = randint(0, len(progression) - 1)
        ans.append(str(progression[index]))
        progression[index] = '..'
        que_array = ''
        for num in progression:
            que_array += ' {ar}'.format(ar=str(num))
        que.append(que_array)
        count += 1
    game(task, que, ans, exp_ans)
