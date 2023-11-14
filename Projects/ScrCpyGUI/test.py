import tkinter as tk
import json

root = tk.Tk()
root.geometry("200x300")

# Create a number list field
num_list = tk.Listbox(root, height=10, width=20)

with open('keyevents.json') as f:
  data = json.load(f)

# Add numbers to the list field
for i in data['key_events']:
    j = data['key_events'][i].split('adb shell input keyevent ')[1]
    print(j, i)
    num_list.insert(j, i)

# Pack the list field
num_list.pack()

# Create a button to get the selected number
get_num_btn = tk.Button(root, text="Get Number", command=lambda: print(num_list.get(num_list.curselection()[0])))

# Pack the button
get_num_btn.pack()

root.mainloop()