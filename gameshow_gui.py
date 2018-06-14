#!/usr/local/bin/python3
"""
Exercise from headfirst book.
Requirements: after a question has been asked, prompt host to press 1 for coreect answer
        2 for wrong
        based on key press, appropriate sound effect
        program remember how many answer correct / wrong
        host will end the quiz by pressing 0. proram then displays # of right/wrong/aksed questions
"""
from tkinter import *
import pygame.mixer
app = Tk()
app.title("TVN Game Show Questions")
app.geometry("300x100+200+100")

b1 = Button(app, text = "Correct", width =10 ) #, color="green"
b1.pack(side = 'left', padx=10, pady=10)
b2 = Button(app, text = "Wrong", width =10) # , color="red"
b2.pack(side = 'right', padx=10, pady=10 )

def wait_finish(channel):
    while channel.get_busy():
        pass
sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound(".\hfprog_sounds\correct.wav")
wrong_s = sounds.Sound(".\hfprog_sounds\wrong.wav")

prompt = "Press 1 for Correct, 2 for Wrong, or 0 to Quit."

count_right = 0
count_wrong = 0
count_questions = 0

choice = input(prompt)
while choice != '0':
    if choice == '1':        
        count_right += 1
        count_questions += 1
        wait_finish(correct_s.play())
    if choice == '2':
        count_wrong +=1
        count_questions +=1
        wait_finish(wrong_s.play())
    choice = input(prompt)
    
print("You asked " + str(count_questions) + " questions.")#.format(count_questions)
print(str (count_right) + " were answered correctly.")#.format(count_right)
print(str(count_wrong) + " were answered incorrectly.")#.format(count_wrong)
app.mainloop()
