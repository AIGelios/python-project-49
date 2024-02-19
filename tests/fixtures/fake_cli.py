import brain_games.cli


def welcome_user():
    print('Welcome to the Brain Games!')
    print('May I have your name? Testuser')
    print('Hello, Testuser!')
    return 'Testuser'


def say_well_done(_):
    brain_games.cli.say_well_done('Testuser')


def say_game_over(_):
    brain_games.cli.say_well_done('Testuser')


def get_user_answer():
    print('Your answer: Correct answer')
    return 'Correct answer'
