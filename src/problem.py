import random


class Problem:
    def __init__(self, problem_type, review_history, problem_examples, next_review):
        self.problem_type = problem_type
        self.review_history = review_history
        self.problem_examples = problem_examples
        self.next_review = next_review

    def review_problem(self):
        """Performs a review of a problem"""
        example_problem = get_example_problem()
        # Display prompt
        # Ask for keypress to display image of solution
        # Then ask for a y/n on whether response was correct
        # Save that response
        pass

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
