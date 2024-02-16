# game engine module

from brain_games.cli import greet_and_get_name, say_well_done, say_game_over


ANSWERS_TO_COMPLETE = 3


def run_game(game_module) -> None:
    '''Take the game resources module and run the game'''
    user = greet_and_get_name()
    print(game_module.description)
    answers_left = ANSWERS_TO_COMPLETE  # the required number of correct answers
    while answers_left > 0:
        question = game_module.generate_question()
        print(f'Question: {question}')
        correct_answer = game_module.get_correct_answer(question)
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            answers_left -= 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            say_game_over(user)
            break
    else:
        say_well_done(user)
