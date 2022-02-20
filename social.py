import random

def welcome_msg():

    welcome = "**SOCIAL: Get to know your fellow members!**\n" \
              "- Type **!social me** and a question will be displayed\n" \
              "- After answering, next user will type **!social me**\n" \
              "- Got it? type **!go** to start"


    return welcome



def social_mode():
    with open("questions.txt") as file:
        questions_array = file.readlines()
    return random_question(questions_array)

def random_question(arr):
    return random.choice(arr)

