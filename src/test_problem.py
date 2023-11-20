from problem import Problem
import pytest

@pytest.fixture
def make_problem():
    return Problem()

def test_get_example_problem():
    assert True