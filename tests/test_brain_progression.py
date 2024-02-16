from brain_games.games.brain_progression import (
    generate_question, get_correct_answer
)


def test_brain_progression():
    for _ in range(3):
        data = generate_question()
        assert isinstance(data, str)
        assert 5 <= len(data.split()) <= 10 
        assert '..' in data
        assert '..' in data.split()
        assert data.count(' ') == len(data.split()) - 1
    assert get_correct_answer('10 15 20 .. 30 35') == '25'
    assert get_correct_answer('3 6 9 12 15 18 ..') == '21'
    assert get_correct_answer('.. 4 6 8 10 12 14 16 18 20') == '2'
