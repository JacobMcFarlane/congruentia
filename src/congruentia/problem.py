import random
import json

from PIL import Image
from datetime import date, datetime, timedelta
from pathlib import Path
from question import Question


class Problem:
    date_format = "%Y-%m-%d"

    def __init__(self, problem_type, review_history, questions, next_review, save_path):
        self.problem_type = problem_type
        self.review_history = review_history
        self.questions = questions
        self.next_review = next_review
        self.save_path = save_path

    def review_problem(self):
        """Performs a review of a problem"""

        example_question = self.get_example_question()

        example_question.review_question()

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

        self.record_response(today, is_correct, example_question.question_id)
        self.update_next_review()
        print(f"Review round complete for {self.problem_type}")

    def get_example_question(self):
        """Gets a problem number to display for review"""
        review_history = [review["problem_ex_id"] for review in self.review_history]

        available_examples = [problem["problem_ex_id"] for problem in self.questions]

        unused_examples = list(set(available_examples) - set(review_history))

        # if any of the examples haven't been used yet, we return one of those examples
        if len(unused_examples) > 0:
            return self.questions[unused_examples[0]]

        # Grab a random problem otherwise
        return self.questions[random.choice(available_examples)]

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

    def save_problem_to_json(self):
        problem_dict = {
            "problem_type": self.problem_type,
            "review_history": self.review_history,
            "next_review": self.next_review,
            "questions": [
                question.save_question_to_json() for question in self.questions
            ],
        }

        problem_dict = json.dumps(problem_dict)

        with open(self.save_path, "w") as outfile:
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
