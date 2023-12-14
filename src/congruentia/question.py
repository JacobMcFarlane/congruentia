import json

from PIL import Image
from datetime import date, datetime, timedelta
from abc import abstractmethod


class Question:
    def __init__(self, question_id, prompt, solution, complexity):
        self.question_id = question_id
        self.prompt = prompt
        self.solution = solution
        self.complexity = complexity

    @abstractmethod
    def review_question(self):
        ...

    @abstractmethod
    def display_question(self):
        ...

    @abstractmethod
    def display_solution():
        ...

    @abstractmethod
    def save_to_json():
        ...


class PNGQuestion(Question):
    question_type = "PNGQuestion"

    def review_question(self):
        self.display_question()

        input("Press any key to see solution")

        self.display_solution()

    def display_question(self):
        prompt = Image.open(self.prompt)
        prompt.show()

    def display_solution(self, solution):
        solution = Image.open(self.solution)
        solution.show()

    def save_to_json(self):
        return {
            "question_id": self.question_id,
            "solution": self.solution,
            "prompt": self.prompt,
            "complexity": self.complexity,
        }
