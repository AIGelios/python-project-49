# resources file for the game "brain-even"
from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question() -> str:
    '''Generate random integer number and return it
    as a string object'''
    return str(randint(1, 100))


def correct_answer(question: str) -> str:
    '''Take integer number as a string and return 'yes' if
    the number is even or 'no' if odd'''
    return 'no' if int(question) % 2 else 'yes'
