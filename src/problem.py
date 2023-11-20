# class problem
class Problem:
    def __init__(self, problem_type, review_history, problem_examples, next_review):
        self.problem_type = problem_type
        self.review_history = review_history
        self.problem_examples = problem_examples 
        self.next_review = next_review

    def review_problem(self):
        """ Performs a review of a problem
        """
        pass

    def get_example_problem(self):
        """ Gets a problem number to display for review
        """
        pass

    def record_response(self):
        """ Transforms user response into an entry in review history
        """
        pass

    def update_next_review(self):
        """Based on review history, updates next review date. 
        """
        #TODO implement spaced repition algo
        
        pass

    

