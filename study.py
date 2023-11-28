# Creates a subject and starts a study session
from congruentia import utils

if __name__ == "__main__":
    utils.subject_from_directory("linear_alg/", "linear_alg/problems/").review_subject()
