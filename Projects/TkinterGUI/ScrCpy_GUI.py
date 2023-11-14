
import os, json
import threading
from tkinter import *

ip = input('''
----------------------------------------
Press `CTRL + PAUSE/BREAK` keys to exit.

Press ENTER for default IP 
    192.168.0.103
----------------------------------------

Paste IP Address of Device : ''')


def task1():
    global ip
    print()

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

    if ip == '':
        ip = '192.168.0.103'

    while True:
        print()
        os.system(f'scrcpy --tcpip={ip}')


def task2():
    print()

    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

    def power():
        os.system(f'adb -s {ip} shell input keyevent 26')

    def volup():
        os.system(f'adb -s {ip} shell input keyevent 24')

    def voldown():
        os.system(f'adb -s {ip} shell input keyevent 25')

    def fun():
        key = num_list.get(num_list.curselection()[0])
        key = key.split(' : ')[0]
        os.system(f'adb -s {ip} shell input keyevent {key}')

    while True:
        root = Tk()
        root.geometry("300x600")
        root.title("ScrCpy GUI")
        root.config(bg="gray")

        num_list = Listbox(root, height=15, width=30)
        with open('keyevents.json') as f:
            data = json.load(f)

        for i in data['key_events']:
            j = data['key_events'][i]
            k = j.split('adb shell input keyevent ')
            num_list.insert(k[1], f'{k[1]} : {i.split("key_")[1]}')

        num_list.place(relx=0.5, rely=0.4, anchor='center')
        get_num_btn = Button(root, bg='green', text="Run ADB", command=fun)
        get_num_btn.place(relx=0.5, rely=0.1, anchor='center')

        VolumeUp = Button(root, text="Volume Up", command=volup)
        VolumeUp.place(relx=0.5, rely=0.7, anchor='center')

        VolumeDown = Button(root, text="Volume Down", command=voldown)
        VolumeDown.place(relx=0.5, rely=0.8, anchor='center')
        
        Power = Button(root, bg='red', text="Power ON / OFF", command=power)
        Power.place(relx=0.5, rely=0.9, anchor='center')
        root.mainloop()


if __name__ == "__main__":
    os.system('color 2')
    print()

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
  
    t1.start()
    t2.start()
  
    t1.join()
    t2.join()
