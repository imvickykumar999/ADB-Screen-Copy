
import os, time

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
# unlock() # passed default passcode
click(x = 40, y = 1270, mess = 'toggle')

for i in range(n): 
    click(x = 250, y = 140, mess = 'undo')

# for i in range(n): 
#     click(x = 360, y = 140, mess = 'redo')

click(x = 40, y = 1270, mess = 'toggle')

for y in range(350, 1101, 250):
    for x in range(107, 612, 168):
        click(x, y)
