class Subject:
    review_list = []

    def __init__(self, problems, max_new_cards, max_review_cards):
        self.problems = problems
        self.max_new_cards = max_new_cards
        self.max_review_cards = max_review_cards

    def review_subject(self):
        self.generate_review_list()
        while len(self.review_list()) > 0:
            problem = self.review_list.pop()
            problem.review_problem()
            self.update_review_list()

        # Determine which cards should be reviewed
        # Display a card from num_new_cards, else get a new problem
        # pop a problem from review list,
        # Determine if card should be added to or removed from problems
        pass

    def generate_review_list(self):
        """Constructs initial ordering of review in review list"""
        pass

    def update_review_list(self):
        """Reorder list after a review based on updated review dates"""
        pass
