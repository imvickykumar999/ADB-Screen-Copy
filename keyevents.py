
# OUTPUT : https://youtube.com/shorts/Tri_bp0lRlQ?feature=share

import os, json

def power_off():
    with open("keyevents.json", "r") as json_file:
        my_dict = json.load(json_file)

    # inp = 'key_power' # to power off mobile
    inp = input('Enter key name : ')

    cmd = my_dict['key_events'][inp]
    os.system(cmd)


inp = 26 # to power off mobile
while inp:
    inp = input('Enter a Sentence : ')

    for i in inp:
        if i == ' ':
            res = 62
        else:
            res = ord(i) - 68

        os.system(f"adb shell input keyevent {res}")
    os.system(f"adb shell input keyevent 66") # enter key

power_off()
