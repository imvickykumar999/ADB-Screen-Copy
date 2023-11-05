
import os, time

x1, y1, x2, y2 = 350, 1250, 400, 0

def unlock(code = 2589):
    time.sleep(2)
    os.system('adb shell input keyevent 26') # Turn ON screen
    os.system(f'adb shell input text {code}') # Input Passcode
    os.system('adb shell input keyevent 66') # Press OK

# unlock()

for x2 in range(0, 800, 100):
    os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}')
