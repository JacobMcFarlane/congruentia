import json
from problem import Problem

def problem_from_json(json_path):
    with open(json_path) as pjson:
        problem_json = json.load(pjson)
    
    
    json_prob = Problem(
        problem_type=problem_json['problem_type'],
        review_history=problem_json['review_history'],
        problem_examples=problem_json['problem_examples'],
        next_review=problem_json['next_review']
    )

    return json_prob