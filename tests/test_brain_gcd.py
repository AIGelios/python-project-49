from brain_games.games.brain_gcd import generate_question, get_correct_answer


def test_brain_gcd():
    for _ in range(3):
        question = generate_question()
        assert ' ' in question
        assert isinstance(question, str)
        data = question.split()
        assert len(data) == 2
        assert data[0].isdigit()
        assert data[1].isdigit()
    assert get_correct_answer('10 15') == '5'
    assert get_correct_answer('17 23') == '1'
    assert get_correct_answer('15 75') == '15'
