# Import tkinker for the user interface  
import tkinter as tk
# Import random to make sure that the correct answer is at least randomly in a b c or d
import random

question_list = [] #questions to be used
# Add main user question input logic
flow_of_the_game = True # variable that checks if the user still wants to add questions or no

while flow_of_the_game:
    option_label = ["a", "b", "c", "d"] #initializes the choices a b c and d which resets after the loop starts again
    question = input("Think of a multiple choice question and input it here (enter nothing if you are done): ") # asks users to add there question, and add blank if they want to stop
    correct_answer = input("input the correct answer: ") #ask user to input the correct answer
    wrong_answers = [input(f"input the incorrect answer 3 times ({i+1}): ") for i in range(3)] #asks the user to input the wrong answer 3 times
    random.shuffle(option_label) #shuffles the options list
    correct_label = option_label[0] #takes only one option from the list
    correct_option = {correct_label: correct_answer} #assigns the correct answer to the label
    incorrect_option = {}
    for index, labels in enumerate(option_label[1:]): # goes through the randomized option labels and assigns the index and the specific label
        incorrect_option[labels] = wrong_answers[index]
    all_options = {**correct_option, **incorrect_option} # merges all the options

    question_data = {"Questions": question,
                     "Options": all_options,
                     "correct answer": correct_option}
    question_list.append(question_data)
    if question:


