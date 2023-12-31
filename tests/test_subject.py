import pytest
from datetime import datetime, date
from congruentia import problem
from congruentia import subject
from congruentia.utils import problem_from_json


@pytest.fixture
def addition_problem():
    return problem_from_json("problem_jsons/example_problem.json")


@pytest.fixture
def subtraction_problem():
    return problem_from_json("problem_jsons/example_problem_2.json")


@pytest.fixture
def future_problem():
    return problem_from_json("problem_jsons/example_problem_future.json")


@pytest.fixture
def basic_math_subject(addition_problem, subtraction_problem, future_problem):
    return subject.Subject([addition_problem, subtraction_problem, future_problem])


@pytest.fixture
def past_date():
    return datetime.strptime("2024-01-11", "%Y-%m-%d")


def test_generate_review_list(basic_math_subject, past_date):
    basic_math_subject.generate_review_list(past_date)
    assert len(basic_math_subject.review_list) == 2


def test_update_review_list(
    basic_math_subject, addition_problem, subtraction_problem, future_problem, past_date
):
    basic_math_subject.review_list = [
        addition_problem,
        subtraction_problem,
        future_problem,
    ]

    basic_math_subject.update_review_list(past_date)
    assert len(basic_math_subject.review_list) == 2
