#!/usr/local/bin/python3
"""slider adjust volume digital music.
Exercise from headfirst book."""
from tkinter import *
import pygame.mixer
from sound_panel import *
import os

app = Tk()
app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()

dirList = os.listdir(".")

for fname in dirList:
    if fname.endswith(".wav"):
        panel = SoundPanel(app, mixer, fname)  
        panel.pack()
"""        
panel = SoundPanel(app, mixer, sound_file = "50459_M_RED_Nephlimizer.wav")
panel.pack()
panel = SoundPanel(app, mixer, sound_file = "49119_M_RED_HardBouncer.wav")
panel.pack()
"""
def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
