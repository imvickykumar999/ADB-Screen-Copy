
import tkinter as tk
import json, os

root = tk.Tk()
ip = '192.168.0.103'

root.geometry("200x300")
num_list = tk.Listbox(root, height=15, width=30)

def fun():
  key = num_list.get(num_list.curselection()[0])
  key = key.split(' : ')[0]
  os.system(f'adb -s {ip} shell input keyevent {key}')

with open('keyevents.json') as f:
  data = json.load(f)

for i in data['key_events']:
  j = data['key_events'][i]

  k = j.split('adb shell input keyevent ')
  num_list.insert(k[1], f'{k[1]} : {i.split("key_")[1]}')

frame = tk.Frame(root) 
frame.pack(pady = 10) 

num_list.pack()
get_num_btn = tk.Button(frame, text="ADB", command=fun)

get_num_btn.pack()
root.mainloop()
