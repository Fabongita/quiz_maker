from tkinter import *
import random
import json 
import subprocess
# Track the quiz state
current_questions = []
current_index = 0
score = 0
# Function for starting the game
def start(questions):
   global current_questions, current_index, score
   current_questions = questions
   current_index = 0
   score = 0
   play_frame.tkraise()

# Function for submitting
def submit():
   pass
# Function for showing the question
def show_question():
   global current_index
   question_data = current_questions[current_index]
   quiz_questions.set(question_data["Questions"])
   selected_answer.set("")
# Function for the quiz making logic the quiz creator button is going to use
def quiz_maker():
    subprocess.call(["python", "quiz_maker_program.py"])
# Function that would serve as the selection for the quizzes in the start button
def load_button():
   selected = start_quiz_listbox.curselection()
   if not selected:
      return  #returns nothing if nothing is selected
   else:
      index = selected[0] 
      quiz_name = start_quiz_listbox.get(index)
      with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
         contents = json.load(file)
         questions_to_play = [question for question in contents if question["Quiz name"] == quiz_name]
      start(questions_to_play)

   start_frame.tkraise()   


# Function for the when the start is pressed that the start button is going to use
def start_button_logic():
    with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
     json_file = json.load(file)
    # Get the unique quiz names
    all_names = [entry["Quiz name"] for entry in json_file]
    unique_name = list(set(all_names))
   
    # Populate the Listbox with quiz names
    quiz_listbox.delete(0, END)
 
    for entry in unique_name:
     start_quiz_listbox.insert(END, entry)
     
    start_frame.tkraise()   

# Function for the saved quizzes the quiz saved quizzes button is going to use
def saved_quizzes():
  # Unload all the contents of questions and answer JSON file
 with open("questions_and_answers.JSON", "r", encoding= "utf-8" ) as file:
    json_file = json.load(file)

    # Get the unique quiz names
    all_names = [entry["Quiz name"] for entry in json_file]
    unique_name = list(set(all_names))

    # Populate the Listbox with quiz names
    quiz_listbox.delete(0, END)
 
 for entry in unique_name:
    quiz_listbox.insert(END, entry)
 saved_quizzes_frame.tkraise()
    
# Open the main window of the tkinter
root = Tk()
root.title("Quiz game")
root.geometry("800x1000")

quiz_questions = StringVar()
#Create a frame for the intro screen, create quizzes screen, start screen, saved quizzes screen, and play screen
intro_frame = Frame(root)
start_frame = Frame(root)
saved_quizzes_frame = Frame(root)
play_frame = Frame(root)

# label for the questions
question_label = Label(play_frame, text= quiz_questions, font="Courier")
question_label.pack(padx="20", pady="20")

# Radio buttons
radiobutton_widgets = {}
selected_answer = StringVar(value="")
options_frame = Frame(play_frame)
options_frame.pack(anchor="w", padx=20, pady=10)
for option_letter in ("a", "b", "c", "d"):
    radio_button = Radiobutton(options_frame, text=f"\u2022 {option_letter.upper()}",
        variable=selected_answer, value=option_letter, indicatoron=True, font=("Courier", 14),
        anchor="w", padx=10)
    radio_button.pack(fill="x", pady="2")
    radiobutton_widgets[option_letter] = radio_button

# Listbox and scrollbar for the saved quizzes of the start button
start_quiz_listbox = Listbox(start_frame, font=("Courier", 12)) 
start_quiz_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
start_scrollbar = Scrollbar(start_frame, orient=VERTICAL, command=start_quiz_listbox.yview)
start_scrollbar.pack(side=RIGHT, fill=Y)
button = Button(start_frame, text="Print Selected", command=load_button)
button.pack()

# connect the listbox and scrollbar
start_quiz_listbox.config(yscrollcommand=start_scrollbar.set)
start_scrollbar.config(command=start_quiz_listbox.yview)

# Configure the listbox and the scrollbar for the saved quizzes 
quiz_listbox = Listbox(saved_quizzes_frame, font=("Courier", 12)) 
quiz_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
scrollbar = Scrollbar(saved_quizzes_frame, orient=VERTICAL, command=quiz_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
# connect the listbox and scrollbar
quiz_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=quiz_listbox.yview)

# Label for the intro screen
ascii_art = """
________        .__           ________                       
\_____  \  __ __|__|_______  /  _____/_____    _____   ____  
 /  / \  \|  |  \  \___   / /   \  ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /  \    \_\  \/ __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \  \______  (____  /__|_|  /\___  >
       \__>              \/         \/     \/      \/     \/ 
                                                                                                                                                                                                                             ░                                                                                                     
"""
intro_label = Label(intro_frame, text=ascii_art, font="Courier")
intro_label.pack(side="top", padx = "20", pady="20")
# Frame to organize buttons
button_frame = Frame(intro_frame)
button_frame.pack(side="bottom", padx="10")

# buttons
quiz_creator_button = Button(button_frame, text="Create Quiz", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=quiz_maker )
quiz_creator_button.pack(padx="10", pady="70", side="left") 
start_button = Button(button_frame, text="Start game", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=start_button_logic )
start_button.pack(padx="10", pady="70", side="left") 
saved_quizzes_button = Button(button_frame, text="Saved Quizzes", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=saved_quizzes )
saved_quizzes_button.pack(padx="10", pady="70", side="left") 

# stack the frames
for frame in (intro_frame, saved_quizzes_frame, start_frame, play_frame):
    frame.place(relwidth=1, relheight=1)

# Call the frame to be used
intro_frame.tkraise()

root.mainloop()
