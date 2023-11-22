import random

from PIL import Image
from datetime import date, datetime, timedelta
from pathlib import Path


class Problem:
    date_format = "%Y-%m-%d"

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

        today = datetime.strftime(date.today(), self.date_format)

        self.record_response(today, is_correct, example_problem["problem_ex_id"])
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
        # Based on SM-0 uses reps of 1, 7, 16, 35, (i - 1) * 2
        # If the last review is wrong, revert to 0

        most_recent_review = datetime.strptime(
            self.review_history[-1]["date"], self.date_format
        )
        span = self.get_last_span()
        if not bool(self.review_history[-1]["is_correct"]) | (span < timedelta(0)):
            self.next_review = most_recent_review
        elif span < timedelta(days=0):
            self.next_review = most_recent_review + timedelta(days=0)
        elif span < timedelta(days=7):
            self.next_review = most_recent_review + timedelta(days=1)
        elif span < timedelta(days=16):
            self.next_review = most_recent_review + timedelta(days=7)
        elif span < timedelta(days=35):
            self.next_review = most_recent_review + timedelta(days=16)
        else:
            self.next_review = most_recent_review + (span - timedelta(days=1)) * 2
        print(f"Next review for: {self.next_review}")
        self.next_review = datetime.strftime(self.next_review, self.date_format)

    def save_problem_to_json(self, save_path):
        problem_dict = {
            "problem_type": self.problem_type,
            "review_history": self.review_history,
            "next_review": self.next_review,
            "problem_examples": self.problem_examples,
        }

        with open(save_path, "w") as outfile:
            outfile.write(problem_dict)

    def get_last_span(self):
        print(len(self.review_history))
        if len(self.review_history) < 2:
            return timedelta(days=-1)
        most_recent_review = datetime.strptime(
            self.review_history[-1]["date"], self.date_format
        )
        second_most_recent_review = datetime.strptime(
            self.review_history[-2]["date"], self.date_format
        )
        return most_recent_review - second_most_recent_review
