import json
import os

from congruentia import subject
from congruentia import problem


def problem_from_json(json_path):
    with open(json_path) as pjson:
        problem_json = json.load(pjson)

    json_prob = problem.Problem(
        problem_type=problem_json["problem_type"],
        review_history=problem_json["review_history"],
        problem_examples=problem_json["problem_examples"],
        next_review=problem_json["next_review"],
    )

    return json_prob


def test_problem(path="problem_jsons/example_problem.json"):
    prob = problem_from_json(path)
    prob.review_problem()


def subject_from_directory(dir_path="problem_jsons/"):
    probs = []
    for problem_path in os.listdir(dir_path):
        probs.append(problem_from_json(f"{dir_path}/{problem_path}"))

    return subject.Subject(probs)


if __name__ == "__main__":
    test_problem()
