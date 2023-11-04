
import os

x1, y1, x2, y2 = 400, 1200, 400, 0

for x2 in range(0, 800, 100):
    os.system(f'''
    adb shell input swipe {x1} {y1} {x2} {y2}
    ''')
