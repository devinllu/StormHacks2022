import random


def social_mode():
    with open("questions.txt") as file:
        questions_array = file.readlines()
    return random_number(questions_array)

def random_number(arr):
    return random.choice(arr)


