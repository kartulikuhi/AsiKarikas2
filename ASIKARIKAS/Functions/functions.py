from playsound import playsound
import os
directory = os.path.dirname(os.path.abspath(__file__))

def play(sound):
    switcher = {
        'win': directory + '/sounds/win_sound.wav',
        'error': directory + '/sounds/error_sound.wav',
        'move': directory + '/sounds/move_sound.wav',
        'tie': directory + '/sounds/draw.wav',
        'start-up': directory + '/sounds/boot.wav'
    }
    playsound(switcher[sound])