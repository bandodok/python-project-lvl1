from random import randint

from brain_games.main_game import game


def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    count = 0
    questions = []
    answers = []
    while count < 3:
        questions.append(randint(1, 100))
        count += 1
    for index in range(0, 3):
        if questions[index] % 2 == 0:
            answers.append('yes')
        else:
            answers.append('no')
    game(task, questions, answers)
