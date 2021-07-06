from brain_games.brain_hello import welcome_user
from brain_games.even_game import brain_even


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if brain_even() == 'win':
        print('Congratulations, {arg1}!'.format(arg1=name))
    else:
        print("Let's try again, {arg1}!".format(arg1=name))


if __name__ == '__main__':
    main()
