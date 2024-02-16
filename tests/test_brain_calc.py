from brain_games.games.brain_calc import generate_question, get_correct_answer


def test_brain_calc():
    for _ in range(3):
        question = generate_question()
        assert isinstance(question, str)
        data = question.split()
        assert data[0].isdigit()
        assert data[1] in ('+', '-', '*')
        assert data[2].isdigit()

    assert get_correct_answer('1 + 1') == '2'
    assert get_correct_answer('15 - 7') == '8'
    assert get_correct_answer('10 * 15') == '150'
