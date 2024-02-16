from brain_games.games.brain_even import generate_question, get_correct_answer


def test_brain_even():
    for _ in range(3):
        question = generate_question()
        assert isinstance(question, str)
        assert question.isdigit()

    for n in ('1', 17.0, 123):
        assert get_correct_answer(n) == 'no'
    for n in ('2', 18.0, 124):
        assert get_correct_answer(n) == 'yes'
