# resources file for the game "brain-gcd"
from random import randint
from math import gcd


description = 'Find the greatest common divisor of given numbers.'


def generate_question() -> str:
    '''Generate 2 random integers and return it as a
    string splitted with space'''
    num_1, num_2 = randint(1, 100), randint(1, 100)
    return f'{num_1} {num_2}'


def correct_answer(question):
    '''Take two integers as a string and return their
    greatest common divisor as a string object'''
    num_1, num_2 = map(int, question.split())
    return str(gcd(num_1, num_2))
