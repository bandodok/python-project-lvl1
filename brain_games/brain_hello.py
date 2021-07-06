import prompt


def welcome_user():
    """Welcome user and ask his name.

    Returns user name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {arg1}'.format(arg1=name))
    return name
