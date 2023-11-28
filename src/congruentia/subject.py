from datetime import date, datetime, timedelta


class Subject:
    review_list = []

    def __init__(self, problems, subproblem_path_prefix="problems/"):
        self.problems = problems
        self.subproblem_path_prefix = subproblem_path_prefix

    def review_subject(self):
        self.generate_review_list(datetime.today())
        while len(self.review_list) > 0:
            problem = self.review_list.pop()
            problem.review_problem(self.subproblem_path_prefix)
            problem.save_problem_to_json()
            self.update_review_list(datetime.today())

    def generate_review_list(self, date_to_check):
        """Constructs initial ordering of review in review list"""
        self.review_list = self._filter_list_on_date(self.problems, date_to_check)

    def update_review_list(self, date_to_check):
        """Reorder list after a review based on updated review dates"""
        self.review_list = self._filter_list_on_date(self.review_list, date_to_check)

    @staticmethod
    def _filter_list_on_date(problem_list, date_to_check):
        updated_list = []
        for subject_problem in problem_list:
            subject_problem_next_review = datetime.strptime(
                subject_problem.next_review, subject_problem.date_format
            )
            if subject_problem_next_review <= date_to_check:
                updated_list.append(subject_problem)
        return updated_list
