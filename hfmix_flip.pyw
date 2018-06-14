#!/usr/local/bin/python3
"""Start and stop digital music.
Exercise from headfirst book."""
from tkinter import *
import pygame.mixer
from time import sleep

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()
flipper = IntVar() #track_playing

def flip_it(): #track_toggle()
    if flipper.get() == 1: #track_playing
        track.play(loops = -1)
        
    else:
        track.stop()
"""
def track_start():
    track.play(loops = -1)

def track_stop():
    track.stop()
"""
def shutdown():
    track.stop()
    app.destroy()
    
track = mixer.Sound(sound_file)

track_button = Checkbutton(app, variable = flipper,
            command = flip_it,
            text = sound_file)
track_button.pack()


"""
start_button = Button(app, command = track_start, text = "start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
"""
app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
