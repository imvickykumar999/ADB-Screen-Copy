
import os, time, sys

def unlock(code = 2589):
    time.sleep(2)
    os.system('adb shell input keyevent 26')
    os.system(f'adb shell input text {code}')
    os.system('adb shell input keyevent 66')
    time.sleep(2)

def click(x, y, mess = 'click'):
    print(f'({mess}) : x, y : {x}, {y}')
    os.system(f'adb shell input tap {x} {y}')

n = 16
print()

# unlock() # passed default passcode
os.system('adb shell input swipe 200 500 200 0') # x1,y1, x2,y2

# click(x = 40, y = 1270, mess = 'toggle')
# print()

# for i in range(n): 
#     click(x = 250, y = 140, mess = 'undo')
# print()

# for i in range(n): 
#     click(x = 360, y = 140, mess = 'redo')
# print()

# click(x = 40, y = 1270, mess = 'toggle')
# print()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    a,b = 1,1

for j, y in enumerate(range(350, 1351, 250)):
    for i, x in enumerate(range(107, 612, 168)):

        if a == i+1 and b == j+1:
            print(f'adb shell input tap {x} {y}')
            click(x, y)


# App Opener ...
'''
python xyClick.py 4 5

adb shell input tap 611 1350
(click) : x, y : 611, 1350
'''
