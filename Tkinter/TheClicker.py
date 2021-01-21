import random
import tkinter as tk
from functools import partial
from tkinter import messagebox

after_id = None
buttons=[]
buttons_index = 0
ordered = random.sample(range(0, 999), 9)
ordered_index = 0
sec = -1
start = True

def start(event=None):     # Start the timer
    global start
    if start:
        start = False
        messagebox.showinfo('info', 'Rule: Click each button in asceding order.\nClick "Ok" to start.')
        run()

def run():                  # Window Timer
    global after_id
    global sec
    sec += 1
    timer.config(text=str(sec))
    after_id = root.after(1000, run)

def change(n):              # Button action
    global after_id
    global buttons_index
    bname = (buttons[n])
    if bname.cget('text') == str(ordered[buttons_index]):
        bname['state'] = tk.DISABLED
        buttons_index += 1
        if buttons_index == len(ordered):
            timer.after_cancel(after_id)
            messagebox.showinfo('info', 'Congratulations!\nScore: '+str(sec)+' seconds')

root = tk.Tk()              # Main window
root.title('Clicker')
root.geometry('+500+200')

for x in range(3):          # Buttons
    for y in range(3):
        n = ordered[ordered_index]
        ordered_index += 1
        btn = tk.Button(root, text=str(n),width = 10)
        btn.grid(row=x, column=y)
        buttons.append(btn)

for i in buttons:
    i.config(command = partial(change,buttons.index(i)))
ordered.sort()

timer = tk.Label(root, text='0', )
timer.grid(row=len(buttons)+1, column = (1))
root.bind("<Button-1>", start)
root.mainloop()