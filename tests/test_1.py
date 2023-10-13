from brain_games.cli import welcome_user, game_over, well_done
import brain_games.games.brain_calc as calc

def test_cli():
    assert welcome_user('Anton') is None
    assert game_over('Anton') is None
    assert well_done('Anton') is None


def test_calc():
    f = calc.correct_answer
    assert f('1 + 1') == '2'
    assert f('2 * 3') == '6'
    assert f('134 - 11') == '123'
