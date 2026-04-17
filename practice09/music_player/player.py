import pygame
import os

BASE_DIR = os.path.dirname(__file__)

playlist = [
    os.path.join(BASE_DIR, "Music/Starboy.mp3"),
    os.path.join(BASE_DIR, "Music/La la la.mp3"),
    os.path.join(BASE_DIR, "Music/Heat Waves.mp3")
]

current_track = 0


def play_track():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()


def stop_track():
    pygame.mixer.music.stop()


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_track()


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_track()


def get_track_name():
    return os.path.basename(playlist[current_track])