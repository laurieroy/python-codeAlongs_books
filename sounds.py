#!/usr/local/bin/python3
"""
Exercise from headfirst book.
Requirements: after a question has been asked, prompt host to press 1 for coreect answer
        2 for wrong
        based on key press, appropriate sound effect
        program remember how many answer correct / wrong
        host will end the quiz by pressing 0. proram then displays # of right/wrong/aksed questions
Pseudocode:
initialize vars: question_count, count_right, count_right = 0,0,0
Greeting/question: Press 1 for correct, 2 for incorrect, 0 to end

while choice != 0
Was answer right?:
get answer(answer):
   
    if right(1):
        play sound
        count_right =+1
        question count =+1
        
    else(2):
        play sound
        count_wrong =+1
        question count =+1
    ask question again
    

print counts to screen
"""
import pygame.mixer
sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s = sounds.Sound(".\hfprog_sounds\heartbeat.wav")
wait_finish(s.play())
s2 = sounds.Sound(".\hfprog_sounds\buzz.wav")
wait_finish(s2.play())
s3 = sounds.Sound(".\hfprog_sounds\ohno.wav")
wait_finish(s3.play())
s4 = sounds.Sound(".\hfprog_sounds\carhorn.wav")
wait_finish(s4.play())

