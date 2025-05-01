from tkinter import *
import random
import json 

# Unload all the contents of questions and answer JSON file
with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
    json_file = json.load(file)
# Randomize the questions
random_question = random.choice(json_file)
# Set the Questions , Options, Correct answer
questions = (random_question["Questions"])
options = (random_question["Options"])
correct_answer = (random_question["correct answer"])
             
# Open the main window of the tkinter
root = Tk()
root.title("Quiz game")
root.geometry("800x1000")
#Add a label for the intro screen
ascii_art = """
________        .__           ________                       
\_____  \  __ __|__|_______  /  _____/_____    _____   ____  
 /  / \  \|  |  \  \___   / /   \  ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /  \    \_\  \/ __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \  \______  (____  /__|_|  /\___  >
       \__>              \/         \/     \/      \/     \/ 
                                                                                                                                                                                                                             ░                                                                                                     
"""
intro_label = Label(root, text=ascii_art, font="Courier")
intro_label.pack(side="top", padx = "20", pady="20")
quiz_creator_button = None 
start_button = None
saved_quizzes_button = None
root.mainloop()
