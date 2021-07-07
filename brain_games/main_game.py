import prompt
from brain_games.brain_hello import welcome_user


def game(task, question, corr_answer):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(task)
    count = 0
    for index in range(0, 3):
        print('Question: {arg1}'.format(arg1=question[index]))
        answer = prompt.string('Your answer: ')
        if answer == corr_answer[index]:
            print('Correct!')
            count += 1
        else:
            print("Let's try again, {arg1}!".format(arg1=name))
            return
    print('Congratulations, {arg1}!'.format(arg1=name))
