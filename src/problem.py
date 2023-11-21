import random

from PIL import Image
from datetime import date
from pathlib import Path


class Problem:
    def __init__(self, problem_type, review_history, problem_examples, next_review):
        self.problem_type = problem_type
        self.review_history = review_history
        self.problem_examples = problem_examples
        self.next_review = next_review

    def review_problem(self, path_prefix="../problems/"):
        """Performs a review of a problem"""

        path = Path(path_prefix)
        example_problem = self.get_example_problem()

        prompt = Image.open(path / example_problem["prompt_path"])
        prompt.show()

        input("Press any key to see solution")

        solution = Image.open(path / example_problem["solution_path"])
        solution.show()

        is_correct = ""
        while not (is_correct == "y" or is_correct == "n"):
            is_correct = input("Was your response correct? (y/n)")
            if not (is_correct == "y" or is_correct == "n"):
                print(f"Input {is_correct} not y/n, please try again")

        if is_correct == "y":
            is_correct = True
        else:
            is_correct = False

        today = date.today()

        self.record_response(str(today), is_correct, example_problem["problem_ex_id"])
        self.update_next_review()
        print(f"Review round complete for {self.problem_type}")

    def get_example_problem(self):
        """Gets a problem number to display for review"""
        review_history = [review["problem_ex_id"] for review in self.review_history]

        available_examples = [
            problem["problem_ex_id"] for problem in self.problem_examples
        ]

        unused_examples = list(set(available_examples) - set(review_history))

        # if any of the examples haven't been used yet, we return one of those examples
        if len(unused_examples) > 0:
            return self.problem_examples[unused_examples[0]]

        # Grab a random problem otherwise
        return self.problem_examples[random.choice(available_examples)]

    def record_response(self, date, is_correct, problem):
        """Transforms user response into an entry in review history"""
        self.review_history.append(
            {"date": date, "is_correct": is_correct, "problem_ex_id": problem}
        )

    def update_next_review(self):
        """Based on review history, updates next review date."""
        # TODO implement spaced repition algo

        pass

    def save_problem_to_json(self, save_path):
        pass
