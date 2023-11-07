
import os, time
from pynput import keyboard
from pynput.keyboard import Key

out = os.popen('adb shell wm size').read()
x, y = out.split()[-1].split('x')

x1 = x2 = int(x)/2
y1, y2 = int(y)*0.65, int(y)*0.15
x3, y3 = x1, int(y)/2

print(f'''
>>> {out}
>>> Menu:

    Up Key    : Next
    Down Key  : Previous
    Left Key  : Like
    Right Key : Dislike
''')

def on_key_release(key):
    global x1, y1, x2, y2, cmd

    if key == Key.up:
        cmd = f'adb shell input swipe {x1} {y1} {x2} {y2}'
        os.system(cmd)

    elif key == Key.down:
        cmd = f'adb shell input swipe {x2} {y2} {x1} {y1}'
        os.system(cmd)

    elif key == Key.left:
        os.system(f'adb shell input tap {x3} {y3}')
        os.system(f'adb shell input tap {x3} {y3}')

    elif key == Key.right:
        os.system(f'adb shell input tap {x3} {y3}')

    elif key == Key.esc:
        exit()

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
