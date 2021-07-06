from random import randint

import prompt


def brain_even():
    count = 0
    while count < 3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = randint(0, 100)
        print('Question: {arg1}'.format(arg1=num))
        ans = prompt.string('Your answer: ')
        if ans == 'yes' and num % 2 == 0 or ans == 'no' and num % 2 != 0:
            print('Correct!')
            count += 1
        else:
            return 'fail'
    return 'win'
