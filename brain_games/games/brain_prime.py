# resources file for the game "brain-prime"
from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    '''Take integer number and return True
    if number is prime, otherwise False'''
    if number == 1:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True


def generate_question() -> str:
    '''Generate random integer number and
    return it as a string object'''
    return str(randint(1, 99))


def get_correct_answer(question: int) -> str:
    '''Take integer number as a string and return "yes"
    if number is prime or "no" if not'''
    return 'yes' if is_prime(int(question)) else 'no'
