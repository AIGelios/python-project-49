import prompt


def username() -> str:
    "Asks user's name and returns it"
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(user: str):
    "Greets user in the game"
    print(f'Hello, {user}!')


def game_over(user: str):
    "Message if the answer was incorrect"
    print(f"Let's try again, {user}!")


def well_done(user: str):
    "Message if the game successfully completed"
    print(f"Congratulations, {user}!")
