from datetime import date, datetime, timedelta


class Subject:
    review_list = []

    def __init__(self, problems):
        self.problems = problems

    def review_subject(self):
        self.generate_review_list()
        while len(self.review_list()) > 0:
            problem = self.review_list.pop()
            problem.review_problem()
            self.update_review_list()

    def generate_review_list(self, date_to_check):
        """Constructs initial ordering of review in review list"""

        self.review_list = [
            problem
            for problem in self.problems
            if datetime.strptime(self.next_review, self.date_format) <= date_to_check
        ]

    def update_review_list(self, date_to_check):
        """Reorder list after a review based on updated review dates"""
        self.review_list = [
            problem
            for problem in self.review_list
            if datetime.strptime(self.next_review, self.date_format) <= date_to_check
        ]
