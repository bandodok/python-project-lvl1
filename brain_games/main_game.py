import prompt
from brain_games.brain_hello import welcome_user


def game(task, question, corr_ans):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(task)
    count = 0
    for index in range(0, 3):
        print('Question: {arg1}'.format(arg1=question[index]))
        answer = prompt.string('Your answer: ')
        if answer == corr_ans[index]:
            print('Correct!')
            count += 1
        else:
            if 'divisor' in task:
                text1 = "'{ar1}' is wrong answer ;(. ".format(ar1=answer)
                text2 = "Correct answer was '{a1}'.".format(a1=corr_ans[index])
                print(text1 + text2)
            print("Let's try again, {arg1}!".format(arg1=name))
            return
    print('Congratulations, {arg1}!'.format(arg1=name))
