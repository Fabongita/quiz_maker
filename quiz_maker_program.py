# Import tkinker for the user interface  
import tkinter as tk
# Import random to make sure that the correct answer is at least randomly in a b c or d
import random

# Add main user question input logic
option_list = ["a", "b", "c", "d"] #initializes the choices a b c and d
flow_of_the_game = True # variable that checks if the user still wants to add questions or no
while flow_of_the_game:
    question = input("Think of a multiple choice question and input it here: ") # asks users to add there question
    correct_answer = input("input the correct answer: ") #ask user to input the correct answer
    wrong_answers = [int(input(f"input the incorrect answer 3 times ({i+1}): ")) for i in range(3)]
    
