
'''
USB DEBUG:
----------

USB Troubleshoot: 
https://stackoverflow.com/a/35642973/11493297


Typing over Wifi: 
https://stackoverflow.com/a/42364486/11493297

>>> adb devices
>>> adb tcpip 5555
>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
>>> adb connect <ip-address>:5555

# Remove USB and test below commands.
>>> adb shell input text connected
>>> adb shell input keyevent 66

Exception : 
ADB Shell commands:
-------------------

adb shell input text '\'
\

adb shell input text '\"'
"

adb shell input text "\'"
'

adb disconnect

OUTPUT:
-------
https://youtube.com/shorts/Tri_bp0lRlQ
https://youtube.com/shorts/uHvtl3Ky0aw
'''

import os
while True: # Ctrl+C to exit.
    text = input('>>> ')

    for i in text:
        if   i == ' ': os.system("adb shell input keyevent 62")
        elif i == '*': os.system("adb shell input keyevent 17")
        elif i == ';': os.system("adb shell input keyevent 74")
        elif i == '(': os.system("adb shell input keyevent 71")
        elif i == ')': os.system("adb shell input keyevent 72")
        # elif i == '?': os.system("adb shell input keyevent 76")

        elif i in ('"', "'"): os.system("adb shell input keyevent 75")
        else: os.system(f'''adb shell input text {i}''')
    input('... ')
    os.system("adb shell input keyevent 66")
