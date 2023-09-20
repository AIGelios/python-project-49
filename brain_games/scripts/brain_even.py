#!/usr/bin/env
# game "Even or not?"

from random import randint
import brain_games.cli as cli
import brain_games.scripts.brain_games as games


def even_num(num: int) -> str:
    "returns True if num is even and False if num is odd"
    return 'yes' if num % 2 == 0 else 'no'


def main():
    "main logics of the game \"Even or not?\""

    games.welcome_to_the_game()
    user = cli.username()
    cli.welcome_user(user)

    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        correct = even_num(question)
        if correct == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct}'.")
            cli.game_over(user)
            break
    else:
        cli.well_done(user)


if __name__ == '__main__':
    main()
