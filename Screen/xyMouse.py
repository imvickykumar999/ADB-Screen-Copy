
import pyautogui, os, time

def unlock(code = 2589):
    time.sleep(2)
    os.system('adb shell input keyevent 26')
    os.system(f'adb shell input text {code}')
    os.system('adb shell input keyevent 66')
    time.sleep(2)

# unlock()
while True:
    pos = pyautogui.position()
    os.system(f'adb shell input tap {pos.x} {pos.y}')
