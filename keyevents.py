
# OUTPUT : 
# https://youtube.com/shorts/Tri_bp0lRlQ?feature=share
# https://youtu.be/uHvtl3Ky0aw

import os, json

def keyevent():
    with open("keyevents.json", "r") as json_file:
        my_dict = json.load(json_file)

    inp=1
    while inp:
        inp = input('Enter key_ or event (tab=61, enter=66) : ')
        if inp == '*':
            break
        try:
            # inp = 'key_power' # to power off mobile
            cmd = my_dict['key_events'][inp]
            os.system(cmd)
        except:
            os.system(f'adb shell input keyevent {inp}')

def typing():
    inp = 26 # to power off mobile
    while inp:
        inp = input('Enter a Sentence : ')
        if inp == '*':
            break
        for i in inp:
            try:
                res = int(i) + 7
            except:
                if i == ' ':
                    res = 62
                else:
                    res = ord(i) - 68
            finally:
                os.system(f"adb shell input keyevent {res}")
        os.system(f"adb shell input keyevent 66") # enter key

print('\nEnter * to break anytime.')
while 1:
    print('\nWelcome to Typing ...')
    typing()
    print('\nWelcome to key_events.')
    keyevent()
