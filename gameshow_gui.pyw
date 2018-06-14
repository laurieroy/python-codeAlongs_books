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

count_right = 0
count_wrong = 0
count_questions = 0


def wait_finish(channel):
    while channel.get_busy():
        pass

def play_correct_sound():
    num_right.set(num_right.get() + 1)
    #count_questions += 1
    wait_finish(correct_s.play())

def play_wrong_sound():
    num_wrong.set(num_wrong.get() +1)
    #count_questions += 1
    wait_finish(wrong_s.play())

app = Tk()
app.title("TVN Game Show Questions")
app.geometry("300x100+200+100")

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound(".\hfprog_sounds\correct.wav")
wrong_s = sounds.Sound(".\hfprog_sounds\wrong.wav")

num_right = IntVar()
num_right.set(0)
num_wrong = IntVar()
num_wrong.set(0)
lab = Label(app, text='When you are ready, click on the buttons!', height =3)
lab.pack()

l1 = Label(app, textvariable = num_right, text= 'Correct Questions', height =3)
l1.pack(side = 'left', pady=10)

l2 =Label(app, textvariable = num_wrong, text= 'Wrong Questions', height =3)
l2.pack(side = 'right', pady=10)

b1 = Button(app, text = "Correct", width =15, command = play_correct_sound ) #, color="green"
b1.pack(side = 'left', padx=10, pady=10)

b2 = Button(app, text = "Wrong", width =15, command = play_wrong_sound) # , color="red"
b2.pack(side = 'right', padx=10, pady=10 )

   
app.mainloop()
        
    
# print("You asked " + str(count_questions) + " questions.")#.format(count_questions)
print(str (count_right) + " were answered correctly.")#.format(count_right)
print(str(count_wrong) + " were answered incorrectly.")#.format(count_wrong)

