import PySimpleGUI as sg
import pause
from pynput.keyboard import Key, Controller

loop = 0
cancel_loop = 0
punch_wait = 0
punch_time = 0
keyboard = Controller()

layout = [[sg.Text("Welcome to David0's autofarm menu!")], [sg.Button("Laser Grids")], [sg.Button("Harvesting With Sorrow")], [sg.Button("Chandeliers")], [sg.Button("Grass/Pepper/Sugar")], [sg.Button("Cancel")]]

window = sg.Window("Autofarming Menu", layout)


def cancel():
    if event == "Cancel":
        loop = 0


def d_press():
    keyboard.press(Key.right)
    pause.milliseconds(punch_time)
    keyboard.release(Key.right)
    pause.milliseconds(punch_wait)
    keyboard.release(Key.space)
    cancel_loop = 1
    return event


def space_press():
    keyboard.press(Key.space)
    pause.milliseconds(1)


def movement():
    d_press()
    space_press()
    loop = 0


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Chandeliers":
        punch_wait = 300
        punch_time = 70
        loop = 1
    if event == "Grass/Pepper/Sugar":
        punch_wait = 300
        punch_time = 100
        loop = 1
    if event == "Laser Grids":
        punch_wait = 300
        punch_time = 85
        loop = 1
    if event == "Harvesting With Sorrow":
        punch_wait = 0
        punch_time = 500
        loop = 1
    while loop == 1:
        movement()
        cancel()
