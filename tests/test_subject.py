import pytest

from congruentia import problem
from congruentia import subject
from congruentia.utils import problem_from_json


@pytest.fixture
def addition_problem():
    return problem_from_json("problem_jsons/example_problem.json")


@pytest.fixture
def subtraction_problem():
    return problem_from_json("problem_jsons/example_problem_2.json")
