
# https://www.instagram.com/p/CzWezAytRPe/

import os, time
from pynput import keyboard
from pynput.keyboard import Key

out = os.popen('adb shell wm size').read()
try: x, y = out.split()[-1].split('x')
except: exit()

x1 = x2 = int(x)/2
y1, y2 = int(y)*0.65, int(y)*0.15
x3, y3 = x1, int(y)/2

print(f'''
>>> {out}
>>> Menu:

    Up    Key : Next     Reel
    Down  Key : Previous Reel
    Left  Key : Like     Reel
    Right Key : Un/Mute  Reel
''')

likes = 0
views = 0
t1 = time.time()

def on_key_release(key):
    global x1, y1, x2, y2, likes, views

    if key == Key.up:
        print('Swipe Up.')
        os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}')
        views += 1

    elif key == Key.down:
        print('Swipe Down.')
        os.system(f'adb shell input swipe {x2} {y2} {x1} {y1}')
        views -= 1

    elif key == Key.left:
        print('Reel Liked.')
        os.system(f'adb shell "input tap {x3} {y3}; input tap {x3} {y3}"')
        likes += 1

    elif key == Key.right:
        print('Reel Un/Muted.')
        os.system(f'adb shell input tap {x3} {y3}')
        time.sleep(0.5)

    elif key == Key.esc:
        t2 = time.time()
        times = int(t2-t1)

        print(f'''
>>> Summary ...

    Total Reels Liked   = {likes}
    Total Reels Watched = {views}
    Time  Spent (sec.)  = {times}
''')
        exit()

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
