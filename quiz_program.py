from tkinter import *
import random
import json 

# Unload all the contents of questions and answer JSON file
with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
    json_file = json.load(file)
# Set the Questions , Options, Correct answer
questions = (json_file["Questions"])
options = (json_file["Options"])
correct_answer = (json_file["correct answer"])
             
# Open the main window of the tkinter
root = Tk()
root.title("Quiz game")
