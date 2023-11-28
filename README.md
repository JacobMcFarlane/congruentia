# Congruentia

Congruentia is a simple python tool for reviewing math concepts with spaced repetition.

Instead of keeping track of a reviews of a specific problem a la Anki, Congruentia tracks your studying across a generally related class of problems. Reviewing from a class of problems translates better to real settings and prevents you from just memorizing the solution to a particular problem.

## Installation

Clone the repo, and install using poetry.

## Usage

If you wnat to use congruentia, I would reccomend forking the repo.

To use the tool in its current state, you need to manually create a set of problem jsons in a folder. Here is an example:

```json
{
    "problem_type": "add_vectors",
    "review_history": [
        ],
    "next_review": "2023-11-29",
    "problem_examples": [
        {
            "problem_ex_id": 0,
            "prompt_path": "addition_1.PNG",
            "solution_path": "addition_1s.PNG"
        },
        {
            "problem_ex_id": 1,
            "prompt_path": "addition_2.PNG",
            "solution_path": "addition_2s.PNG"
        },
        {
            "problem_ex_id": 2,
            "prompt_path": "addition_3.PNG",
            "solution_path": "addition_3s.PNG"
        }
    ]
}
```

Use a meaningful name for problem type, and replace the prompt and solution paths with the names of the files with and without the prompt paths.

Update study.py to point at the folders with the problem jsons and PNGs and call from the root of the repo:

```bash
python study.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
