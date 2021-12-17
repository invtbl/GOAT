
import time

global correct

correct = ["kobe", "Kobe", "kobe bryant", "Kobe Bryant"]

def continue_loop():
    prompt = input("Would you like to run the program again? y for yes or n for no: ")
    prompt = prompt.strip()

    while prompt not in ["y", "n", "Y", "N"]:
        prompt = input("Would you like to run the program again? y for yes or n for no: ")

    if prompt == "y":
        true_Goat()
    elif prompt == "n" and question in correct:
        time.sleep(2)
        print("Thank you for having sense!")
    elif prompt == "n" and question not in correct:
        time.sleep(3)
        print("Thank you for wasting my time!")

def true_Goat():
    global question
    question = input("Who is the greatest basketball player of all time: ")
    question = question.strip()

    if question not in correct:
        time.sleep(2)
        print(" -_- ...No")
        continue_loop()
    else:
        time.sleep(3)
        print("You're damn right it is!")
        continue_loop()

true_Goat()
