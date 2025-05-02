from tkinter import *
import random
import json 

# Function for the quiz making logic the quiz creator button is going to use
def quiz_maker():
    pass

# Function for the when the start is pressed that the start button is going to use
def start_button_logic():
    pass

# Function for the saved quizzes the quiz saved quizzes button is going to use
def saved_quizzes():
    pass
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

#Create a frame for the intro screen, create quizzes screen, start screen, and saved quizzes screen
intro_frame = Frame(root)
create_quizzes_frame = Frame(root)
saved_quizzes_frame = Frame(root)

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
# Frame to organize buttons
button_frame = Frame(root)
button_frame.pack(side="bottom", padx="10")

# buttons
quiz_creator_button = Button(button_frame, text="sheesh bro", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=quiz_maker )
quiz_creator_button.pack(padx="10", pady="70", side="left") 
start_button = Button(button_frame, text="I am steve", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=start_button_logic )
start_button.pack(padx="10", pady="70", side="left") 
saved_quizzes_button = Button(button_frame, text="SPAM", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=saved_quizzes )
saved_quizzes_button.pack(padx="10", pady="70", side="left") 

root.mainloop()
