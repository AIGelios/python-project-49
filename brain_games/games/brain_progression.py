# resources file for the game "brain-progression"
from random import randint, randrange


description = 'What number is missing in the progression?'


def generate_question() -> str:
    '''Generate arithmetic progression with one lost number
    and return it as a string object'''
    start, step, length = randint(1, 50), randint(1, 10), randint(5, 10)
    progression = list(range(start, start + step * length, step))
    progression[randrange(length)] = '..'  # changing random item with 2 dots
    return ' '.join(str(x) for x in progression)


def get_correct_answer(question: str) -> str:
    '''Take ariphmetic progression of integer numbers splitted by
    spaces, find and return the lost number as a string object'''
    q = question.split()  # q - question as list
    i = q.index('..')  # i - index of '..'
    if i >= 2:  # getting lost num from previous nums if they exist
        lost_num = 2 * int(q[i - 1]) - int(q[i - 2])
    else:  # getting lost num from next nums
        lost_num = 2 * int(q[i + 1]) - int(q[i + 2])
    return str(lost_num)
