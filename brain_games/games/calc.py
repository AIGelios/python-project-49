from random import randint, choice
from operator import add, sub, mul


description = 'What is the result of the expression?'


operators = {'+': add, '-': sub, '*': mul}


def generate_question():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    operation = choice(list(operators))
    return f'{num_1} {operation} {num_2}'


def correct_answer(question):
    num_1, op, num_2 = question.split()
    num_1, num_2 = int(num_1), int(num_2)
    operation = operators[op]
    return str(operation(num_1, num_2))
