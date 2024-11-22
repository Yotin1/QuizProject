# module used for clearing the terminal
from os import system, name
import random as r
import questions as q

# loads questions stored in a seperate file
questions = q.questions
# initialises list category names
category_names = ["General Knowledge"]
for key in questions.keys():
    category_names.append(key)

# function to clear screen
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# function to load the start screen
def start_menu():
    clear()
    print("- Quiz -")
    print("Welcome to the quiz!")
    return input("Press enter to start or type \"q\" to quit: ")
    
# function to allow the user to select a category
def select_category():
    clear()
    while True:
        print("- Categories -")
        for index, value in enumerate(category_names):
            print(f"{index + 1}. {value}")
        selection = input("Please choose a category: ")
        global selected_category
        # allows the user to type the option number or the category name and checks if the input is valid
        if selection.isdigit():
            try:
                selected_category = category_names[int(selection) - 1]
            except IndexError:
                print("Invalid category selected, Please try again")
            else:
                break
        elif selection.casefold() in (i.casefold() for i in category_names):
            selected_category = category_names[[i.casefold() for i in category_names].index(selection.casefold())]
            break
        clear()
        print("Invalid category selected, Please try again")
    clear()
    print(f"You have chosen \"{selected_category}\"")
    input("Press enter to start")

# function that runs the quiz section
def quiz():
    # if general knowledge is selected, questions from all categories will be picked
    if selected_category == category_names[0]:
        category_questions = {}
        for i in range(len(category_names) - 1):
            category_questions.update(list(questions.values())[i])
    else:
        category_questions = questions[selected_category]
    random_ids = r.sample(range(len(category_questions)), k=10)
    random_questions = []
    letters = ["A", "B", "C", "D"]
    for id in random_ids:
        random_questions.append(list(category_questions.items())[id])
    question_num = 1
    score = 0
    for question in random_questions:
        clear()
        correct_answer = ""
        print(f"{question_num}. {question[0]}")
        options = list(question[1].keys())
        # shuffles the order the answers appear in the terminal
        r.shuffle(options)
        for i in range(len(options)):
            if question[1][options[i]] is True:
                correct_answer = f"{letters[i]}. {options[i]}"
            print(f"    {letters[i]}. {options[i]}")
        answer = input("Answer: ")
        if answer.upper() == correct_answer[0].upper():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect, the answer was \"{correct_answer}\"")
        input("Press enter to continue")
        question_num += 1
    clear()
    print("Quiz Over")
    print(f"You got {score}/{question_num - 1} questions correct")
    input("Press enter to return to the main menu")

# allows the user to keep playing unless they quit at the start screen
while True:
    if start_menu().upper() == "Q":
        break
    select_category()
    quiz()

