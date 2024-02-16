from brain_games.games.brain_prime import generate_question, get_correct_answer


def test_brain_prime():
    for _ in range(3):
        data = generate_question()
        assert isinstance(data, str)
        assert data.isdigit()

    for n in ('6', '22', '95'):
        assert get_correct_answer(n) == 'no'
    for n in ('3', '17', '41'):
        assert get_correct_answer(n) == 'yes'
