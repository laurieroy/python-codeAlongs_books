#!/usr/local/bin/python3
"""adjust volume digital music.
Exercise from headfirst book."""
from tkinter import *
import pygame.mixer
from time import sleep

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)
print("PLay it LOUD, man!")
track.play(loops = -1)
track.set_volume(0.9)
sleep(2)
print("Softly does it...")
track.set_volume(0.1)
sleep(2)
track.stop()
