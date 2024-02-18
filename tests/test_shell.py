from contextlib import redirect_stdout
import io
from brain_games.shell import run_game
from .fixtures import fake_cli, fake_game


test_output = '''Welcome to the Brain Games!
May I have your name? Testuser
Hello, Testuser!
Description
Question: Question
Your answer: Correct answer
Correct!
Question: Question
Your answer: Correct answer
Correct!
Question: Question
Your answer: Correct answer
Correct!
Congratulations, Testuser!
'''


def test_run_game():
    output_getter = io.StringIO()
    with redirect_stdout(output_getter):
        run_game(game_module=fake_game, cli_module=fake_cli)
    output = output_getter.getvalue()
    assert output == test_output
