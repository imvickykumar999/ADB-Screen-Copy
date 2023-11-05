
import os

def undo(x = 250, y = 150):
    os.system(f'adb shell input tap {x} {y}')

def click(x, y):
    os.system(f'adb shell input tap {x} {y}')


undo()
x, y = 100, 200
click(x, y)
