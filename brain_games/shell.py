# game engine module

import brain_games.scripts.brain_games as start
import brain_games.cli as cli


def game_shell(game_module):
    start.welcome()
    user = cli.username()
    cli.welcome_user(user)
    print(game_module.description)
    answers_to_complete = 3
    while answers_to_complete != 0:
        question = game_module.generate_question()
        print(f'Question: {question}')
        correct_answer = game_module.correct_answer(question)
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            answers_to_complete -= 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            cli.game_over(user)
            break
    else:
        cli.well_done(user)
