"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [1], "answer": 1},
        {"input": [2], "answer": 3},
        {"input": [3], "answer": 6},
        {"input": [4], "answer": 10},
        {"input": [5], "answer": 15},
        {"input": [10], "answer": 55},
        {"input": [20], "answer": 210},
        {"input": [100], "answer": 5050},
        {"input": [200], "answer": 20100},
        {"input": [500], "answer": 125250},
    ],
    "Extra": [
        {"input": [900], "answer": 405450},
        {"input": [461], "answer": 106491},
    ]
}
