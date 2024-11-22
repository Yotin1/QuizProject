from os import system, name
import random as r
import questions as q

questions = q.questions
category_names = [0] * (len(questions) + 1)
category_names[0] = "General Knowledge (WIP)"
for key, value in questions.items():
    category_names[value["ID"] - 1] = key

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def start_menu():
    clear()
    print("- Quiz -")
    input("Welcome to the quiz game! Press enter to start")
    
def select_category():
    clear()
    while True:
        print("- Categories -")
        for index, value in enumerate(category_names):
            print(f"{index + 1}. {value}")
        selection = input("Please choose a category: ")
        global selected_category
        if selection.isdigit() and selection != "1":
            selected_category = category_names[int(selection) - 1]
            break
        elif selection.casefold() in (i.casefold() for i in category_names):
            selected_category = category_names[[i.casefold() for i in category_names].index(selection.casefold())]
            if selected_category.casefold() != category_names[0].casefold():
                break
        clear()
        print("Invalid category selected, Please try again")
    clear()
    print(f"You have chosen \"{selected_category}\"")
    input("Press enter to start")

def quiz():
    selected_category = "Science"
    category_questions = questions[selected_category]
    category_questions.pop("ID")
    random_questions = []
    for i in range(10):
        random_questions.append(r.choice(list(category_questions.items())))
        category_questions.pop(random_questions[i][0])
    question_num = 1
    score = 0
    for question in random_questions:
        clear()
        correct_answer = ""
        print(f"{question_num}. {question[0]}")
        for option in question[1].keys():
            if question[1][option] is True:
                correct_answer = option
            print(f"    {option}")
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

start_menu()
select_category()
quiz()
