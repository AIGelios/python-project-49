# a module with functions for interaction with user
import prompt


def greet_and_get_name() -> str:
    "Greet user, ask his/her name and return it"
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def say_game_over(user: str) -> str:
    "Say goodbye to user when the answer was incorrect"
    print(f"Let's try again, {user}!")


def say_well_done(user: str) -> str:
    "Say goodbye to user when all answers was correct"
    print(f"Congratulations, {user}!")
