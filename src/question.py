import json

from PIL import Image
from datetime import date, datetime, timedelta


class Question:
    def __init__(self, question_id, question, solution, complexity):
        self.question_id = question_id
        self.question = question
        self.solution = solution
        self.complexity = complexity

    @abstractmethod
    def review_question(self):
        pass

    @bstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def display_solution():
        pass


class PNGQuestion(Question):
    question_type = "PNGQuestion"

    def review_question(self):
        self.display_question()

        input("Press any key to see solution")

        self.display_solution()

    def display_question(self):
        prompt = Image.open(self.question)
        prompt.show()

    def display_solution(self, solution):
        solution = Image.open(self.solution)
        solution.show()
