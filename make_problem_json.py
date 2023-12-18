import os
from pathlib import Path
from congruentia import problem
from congruentia import utils

import unicodedata
import re


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def fetch_problem_template():
    problem_template = {
        "problem_type": "add_vectors",
        "review_history": [],
        "next_review": "2023-12-11",
        "questions": [],
    }
    return problem_template


def fetch_question_template():
    question_template = {
        "question_id": 0,
        "question_type": "LLMQuestion",
        "solution": "",
        "prompt": "",
        "complexity": 1,
    }
    return question_template


if __name__ == "__main__":
    problem_template = fetch_problem_template()

    problem_type = input("Please enter the name of the problem type:")
    problem_template["problem_type"] = problem_type

    question_prompt = ""
    question_id = 0
    questions = []

    while True:
        question_prompt = input(
            "Please enter prompt(s). Enter 'done' once you are finished"
        )

        if question_prompt == "done":
            break

        question_template = fetch_question_template()
        question_template["question_id"] = question_id
        question_template["prompt"] = question_prompt
        question_id = question_id + 1
        questions.append(question_template)

    problem_template["questions"] = questions

    json_prob = problem.Problem(
        problem_type=problem_template["problem_type"],
        review_history=problem_template["review_history"],
        questions=[utils.question_from_json(q) for q in problem_template["questions"]],
        next_review=problem_template["next_review"],
        save_path=Path(os.getcwd(), slugify(problem_type) + ".json"),
    )

    json_prob.save_problem_to_json()
