# Import tkinker for the user interface  
from tkinter import *
from tkinter import ttk, simpledialog  #added simple dialogue for simple user interaction
# Import random to make sure that the correct answer is at least randomly in a b c or d
import random

# Setup main window
root = Tk()
root.title("Create your own quiz game")
root.geometry("750x250")

question_list = [] #questions to be used

# Add main user question input logic
flow_of_the_game = True # variable that checks if the user still wants to add questions or no
def questions_options_answers():
    while flow_of_the_game:
        option_label = ["a", "b", "c", "d"] #initializes the choices a b c and d which resets after the loop starts again
        question = simpledialog.askstring("input question", "Think of a multiple choice question and input it here (enter nothing if you are done): ") # asks users to add there question, and add blank if they want to stop
        
        if not question: #checks if the input in the question variable is a space or not
        
            #add a file handling logic that collects the data from the questions list to a text file
         with open("questions_and_answers.txt", "w") as file:
            for items in question_list: #iterates through the items inside the question list
                file.write("Question: " + items["Questions"] + "\n") #specifically prints the question 
                for label, options in sorted(items["Options"].items()): 
                    file.write(f"{label.upper()}  {options} \n") #prints the choices
                for label, answers in(items["correct answer"].items()): #iterates through the items inside the correct answers list
                    file.write("correct answer " + label.upper() + ": " + answers + "\n") #Prints the correct answer inside the text file

            break #breaks the whole loop
        correct_answer = simpledialog.askstring("Input correct answer", "input the correct answer: ") #ask user to input the correct answer

        wrong_answers = []
        #create a for loop that repeats the askstring function 3 times
        for i in range(3):
           simple_dialogue_answer = simpledialog.askstring("3 incorrect answers input ", f"Please input the wrong answer 3 times ({i+1} times inputted): ")
           if simple_dialogue_answer is None: # checks if the answer is blank
              simple_dialogue_answer = "" #converts the blank into space
           wrong_answers.append(simple_dialogue_answer) #appends the answers into the wrong answer list

        if len(wrong_answers) != 3: # checks if the wrong answers are not exactly 3
           print("Please input exactly 3 answers")
           return 
        
        random.shuffle(option_label) #shuffles the options list
        
        correct_label = option_label[0] #takes only one option from the list
        
        correct_option = {correct_label: correct_answer} #assigns the correct answer to the label
        
        incorrect_option = {}
        
        for index, label in enumerate(option_label[1:]): # goes through the randomized option labels and assigns the index and the specific label
            incorrect_option[label] = wrong_answers[index]
        
        all_options = {**correct_option, **incorrect_option} # merges all the options

        question_data = {"Questions": question,
                        "Options": all_options,
                        "correct answer": correct_option}
    
        question_list.append(question_data)
button = Button(root, text="Press if you want to start adding questions", command=questions_options_answers)
button.pack(pady=40)
root.mainloop()





