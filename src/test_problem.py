import pytest
import os

from problem import Problem


def problem_from_json(json_path):
    json_path


@pytest.fixture
def addition_problem():
    problem_dict = {
        "problem_type": "addition",
        "review_history": [
            {"date": "20/11/2023", "is_correct": True, "problem_ex_id": 1}
        ],
        "next_review": "11/21/2023",
        "problem_examples": [
            {
                "problem_ex_id": 0,
                "prompt_path": "add1.png",
                "solution_path": "add1s.png",
            },
            {
                "problem_ex_id": 1,
                "prompt_path": "add2.png",
                "solution_path": "add2s.png",
            },
        ],
    }

    json_prob = Problem(
        problem_type=problem_dict["problem_type"],
        review_history=problem_dict["review_history"],
        problem_examples=problem_dict["problem_examples"],
        next_review=problem_dict["next_review"],
    )
    return json_prob


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
            [{"date": "20/11/2023", "is_correct": True, "problem_ex_id": 1}],
            "20/11/2023",
        ),
        (
            [{"date": "20/11/2023", "is_correct": True, "problem_ex_id": 1}],
            "21/11/2023",
        ),
        (
            [
                {"date": "20/11/2023", "is_correct": True, "problem_ex_id": 1},
                {"date": "21/11/2023", "is_correct": True, "problem_ex_id": 2},
            ],
            "28/11/2023",
        ),
        (
            [
                {"date": "20/11/2023", "is_correct": True, "problem_ex_id": 1},
                {"date": "21/11/2023", "is_correct": False, "problem_ex_id": 2},
            ],
            "22/11/2023",
        ),
        (
            [
                {"date": "20/9/2023", "is_correct": True, "problem_ex_id": 1},
                {"date": "20/11/2023", "is_correct": False, "problem_ex_id": 2},
            ],
            "19/04/2023",
        ),
    ],
)
def test_spaced_algo(history, result):
    prob = Problem("", history, "", "")
    prob.update_next_review()
    assert prob.next_review == result
