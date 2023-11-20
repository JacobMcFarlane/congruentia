from src.problem import Problem
import pytest

@pytest.fixture
def make_problem():
    return Problem()

class TestProblem:
    def test_get_example_problem():
        pass