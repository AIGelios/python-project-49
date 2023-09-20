from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    return str(randint(1, 100))


def correct_answer(question):
    return 'no' if int(question) % 2 else 'yes'
