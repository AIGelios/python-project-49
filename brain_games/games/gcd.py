from random import randint
from math import gcd


description = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    return f'{num_1} {num_2}'


def correct_answer(question):
    num_1, num_2 = map(int, question.split())
    return str(gcd(num_1, num_2))
