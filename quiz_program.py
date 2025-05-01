from tkinter import *
import random
import json 

# Unload all the contents of questions and answer JSON file
with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
    json_file = json.load(file)
print(json_file)
# Open the main window of the tkinter