
'''
USB DEBUG:
---------
https://stackoverflow.com/a/35642973/11493297

ADB Shell commands:
------------------
adb shell input text '\"'
adb shell input text "\'"

OUTPUT:
------ 
https://youtube.com/shorts/Tri_bp0lRlQ
https://youtube.com/shorts/uHvtl3Ky0aw
'''

import os

while True:
    text = input('>>> ').split()

    for i in text:
        if i == '*':
            os.system("adb shell input keyevent 17")
        else:
            os.system(f'''adb shell input text "{i}"''')
            
        os.system("adb shell input keyevent 62")
    os.system("adb shell input keyevent 66")
