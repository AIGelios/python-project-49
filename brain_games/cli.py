# a module with functions for interaction with user
import prompt


def username() -> str:
    "Ask user's name and return it for further use"
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(user: str):
    "Greet user in the game"
    print(f'Hello, {user}!')


def game_over(user: str):
    "Say goodbye to user when the answer was incorrect"
    print(f"Let's try again, {user}!")


def well_done(user: str):
    "Say goodbye to user when all answers was correct"
    print(f"Congratulations, {user}!")
