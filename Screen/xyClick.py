
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

# row 1st ...
click(108, 350) # 1st icon
click(275, 350) # 2nd icon
click(444, 350) # 3rd icon
click(610, 350) # 4th icon

# row 2nd ...
click(108, 600) # 5th icon
click(275, 600) # 2nd icon
click(444, 600) # 3rd icon
click(610, 600) # 1st icon

# row 3rd ...
click(108, 851) # 5th icon
click(275, 851) # 2nd icon
click(444, 851) # 3rd icon
click(610, 851) # 1st icon

# row 4th ...
click(108, 1100) # 5th icon
click(275, 1100) # 2nd icon
click(444, 1100) # 3rd icon
click(610, 1100) # 1st icon
