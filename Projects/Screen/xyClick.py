
import os, time, sys

def unlock(code = 2589):
    print('\nUnlocking Device ...')
    time.sleep(2)
    
    os.system('adb shell input keyevent 26')
    os.system(f'adb shell input text {code}')
    os.system('adb shell input keyevent 66')
    time.sleep(2)

def click(x, y, mess = 'clicked'):
    print(f'({mess}) : x, y : {x}, {y}')
    os.system(f'adb shell input tap {x} {y}')


# click(x = 40, y = 1270, mess = 'toggle')
# print()

# n = 16
# for i in range(n): 
#     click(x = 250, y = 140, mess = 'undo')
# print()

# for i in range(n): 
#     click(x = 360, y = 140, mess = 'redo')
# print()

# click(x = 40, y = 1270, mess = 'toggle')
# print()


unlock() # passed default passcode
os.system('adb shell input swipe 200 500 200 0') # x1,y1, x2,y2
print()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    a,b = 1,1

for j, y in enumerate(range(350, 1351, 250)):
    for i, x in enumerate(range(107, 612, 168)):

        if a == i+1 and b == j+1:
            print(f'>>> adb shell input tap {x} {y}')
            click(x, y)

if a == 1 and b == 1:
    os.system('adb shell input swipe 500 1000 0 1000') # swipe left


# App Opener ...
'''
python xyClick.py 1 3

>>> adb shell input tap 107 850
(clicked) : x, y : 107, 850
'''
