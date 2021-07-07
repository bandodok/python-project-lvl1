from random import randint, choice

from brain_games.main_game import game


def brain_calc():
    task = 'What is the result of the expression?'
    count = 0
    questions = []
    answers = []
    while count < 3:
        first_num = randint(0, 100)
        second_num = randint(0, 100)
        sign = choice(('+', '-', '*'))
        questions.append('{arg1} {arg2} {arg3}'.format(arg1=first_num, arg2=sign, arg3=second_num))
        count += 1
        if sign == '+':
            answers.append(str(first_num + second_num))
        elif sign == '-':
            answers.append(str(first_num - second_num))
        elif sign == '*':
            answers.append(str(first_num * second_num))
    game(task, questions, answers)
