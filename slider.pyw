#!/usr/local/bin/python3
"""slider adjust volume digital music.
Exercise from headfirst book."""
from tkinter import *
import pygame.mixer

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()

track = mixer.Sound(sound_file)
track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing,
                           command = track_toggle,
                           text = sound_file)
track_button.pack(side = LEFT)

def track_toggle():
    if track_playing_get() == 1:
        track.play(loops = -1)
    else:
        track.stop()
def current_volume():
    track.set_volume(0.3) # starting value

def shutdown()
    track.stop()
    app.destroy()

volume = DoubleVar()
volume_scale = Scale(app,
                     variable = volume,
                     from_      = 0.0,
                     to         = 1.0,
                     resolution = 0.1,
                     command    = change_volume,
                     label      = "Volume",
                     orient     = HORIZONTAL)

volume_scale.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
