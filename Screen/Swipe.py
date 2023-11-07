
import os
from pynput import keyboard
from pynput.keyboard import Key

out = os.popen('adb shell wm size').read()
x, y = out.split()[-1].split('x')

x1 = x2 = int(x)/2
y1, y2 = int(y)*0.65, int(y)*0.15

def on_key_release(key):
    global x1, y1, x2, y2, cmd

    if key == Key.up:
        print(f'({x1}, {y1}) -> ({x2}, {y2})')
        cmd = f'adb shell input swipe {x1} {y1} {x2} {y2}'

    elif key == Key.down:
        print(f'({x1}, {y1}) <- ({x2}, {y2})')
        cmd = f'adb shell input swipe {x2} {y2} {x1} {y1}'

    elif key == Key.esc:
        exit()
    os.system(cmd)

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
