
import os, time

def unlock(code = 2589):
    time.sleep(2)
    os.system('adb shell input keyevent 26') # Turn ON screen
    os.system(f'adb shell input text {code}') # Input Passcode
    os.system('adb shell input keyevent 66') # Press OK
    time.sleep(2)

def click(x, y):
    print(f'x, y : {x}, {y}')
    os.system(f'adb shell input tap {x} {y}')

# unlock()

click(x = 250, y = 150) # undo
# click(x = 360, y = 150) # redo

click(x = 80, y = 1210) # toggle
# for i in range(4): undo()

# # row 1st ...
# click(108, 350) # 1st icon
# click(275, 350) # 2nd icon
# click(444, 350) # 3rd icon
# click(610, 350) # 4th icon

# # row 2nd ...
# click(108, 600) # 5th icon
# click(275, 600) # 2nd icon
# click(444, 600) # 3rd icon
# click(610, 600) # 1st icon

# # row 3rd ...
# click(108, 851) # 5th icon
# click(275, 851) # 2nd icon
# click(444, 851) # 3rd icon
# click(610, 851) # 1st icon

# # row 4th ...
# click(108, 1100) # 5th icon
# click(275, 1100) # 2nd icon
# click(444, 1100) # 3rd icon
# click(610, 1100) # 1st icon
