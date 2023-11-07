
import os

x1 = x2 = 350
y1, y2 = 1100, 200

# y1, y2 = y2, y1 # swipe down
os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}') # x1,y1, x2,y2


'''
adb shell wm size
Physical size: 720x1600
'''
