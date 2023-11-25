import pytest

from congruentia import problem
from congruentia import utils


def problem_from_json(json_path):
    json_path


@pytest.fixture
def addition_problem():
    return utils.problem_from_json("problem_jsons/example_problem.json")


def test_get_example_problem(addition_problem):
    assert addition_problem.get_example_problem()["problem_ex_id"] == 0


def test_record_response(addition_problem):
    addition_problem.record_response("19/1/2030", True, 8)
    assert addition_problem.review_history[-1] == {
        "date": "19/1/2030",
        "is_correct": True,
        "problem_ex_id": 8,
    }


@pytest.mark.parametrize(
    "history,result",
    [
        (
            [{"date": "2023-11-20", "is_correct": True, "problem_ex_id": 1}],
            "2023-11-20",
        ),
        (
            [
                {"date": "2023-11-20", "is_correct": True, "problem_ex_id": 1},
                {"date": "2023-11-20", "is_correct": True, "problem_ex_id": 2},
            ],
            "2023-11-21",
        ),
        (
            [
                {"date": "2023-11-21", "is_correct": True, "problem_ex_id": 1},
                {"date": "2023-11-21", "is_correct": False, "problem_ex_id": 2},
            ],
            "2023-11-21",
        ),
        (
            [
                {"date": "2023-09-20", "is_correct": True, "problem_ex_id": 1},
                {"date": "2023-11-21", "is_correct": True, "problem_ex_id": 2},
            ],
            "2024-03-22",
        ),
    ],
)
def test_spaced_algo(history, result):
    prob = problem.Problem("2020-01-01", history, "", "")
    prob.update_next_review()
    assert prob.next_review == result
