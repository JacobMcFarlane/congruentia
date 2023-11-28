import json
import os

from congruentia import subject
from congruentia import problem


def problem_from_json(json_path):
    print(json_path)
    with open(json_path) as pjson:
        problem_json = json.load(pjson)

    json_prob = problem.Problem(
        problem_type=problem_json["problem_type"],
        review_history=problem_json["review_history"],
        problem_examples=problem_json["problem_examples"],
        next_review=problem_json["next_review"],
        save_path=json_path,
    )

    return json_prob


def test_problem(path="problem_jsons/example_problem.json"):
    prob = problem_from_json(path)
    prob.review_problem()


def subject_from_directory(dir_path="problem_jsons/", sub_problems_path="problems/"):
    probs = []
    for problem_path in os.listdir(dir_path):
        if problem_path.endswith(".json"):
            probs.append(problem_from_json(f"{dir_path}{problem_path}"))

    return subject.Subject(probs, sub_problems_path)


if __name__ == "__main__":
    test_problem()
