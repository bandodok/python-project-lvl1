import prompt
from brain_games.brain_hello import welcome_user


def game(task, question, corr_ans, ex_ans=False):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(task)
    for i, q in enumerate(question):
        print(f'Question: {q}')
        answer = prompt.string('Your answer: ')
        if answer == corr_ans[i]:
            print('Correct!')
            continue
        if ex_ans:
            text1 = f"'{answer}' is wrong answer ;(. "
            text2 = f"Correct answer was '{corr_ans[i]}'."
            print(text1 + text2)
        print(f"Let's try again, {name}!")
        return
    print(f'Congratulations, {name}!')
