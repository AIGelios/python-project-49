# resources file for the game "brain-calc"
from random import randint, choice
from operator import add, sub, mul


description = 'What is the result of the expression?'


operators = {'+': add, '-': sub, '*': mul}


def generate_question() -> str:
    '''Generate random arithmetic operation between
    two integers and return it as a string object'''
    num_1, num_2 = randint(1, 100), randint(1, 100)
    operation = choice(list(operators))
    return f'{num_1} {operation} {num_2}'


def get_correct_answer(question: str) -> str:
    '''Take an arithmetic operation as a string and return
    the right solution as a string object'''
    num_1, op, num_2 = question.split()
    num_1, num_2 = int(num_1), int(num_2)
    result = operators[op](num_1, num_2)
    return str(result)
