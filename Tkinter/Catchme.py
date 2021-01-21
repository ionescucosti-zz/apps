import tkinter as tk
from random import randint

root = tk.Tk()
root.title('Catch me if you can!')
root.minsize(500, 500)
root.geometry("+500+150")

def run(e):
    width=randint(0,435)
    heigth=randint(0,475)
    button.place(x=width,y=heigth)

button = tk.Button(root, text='Catch me!')
button.place(x=0,y=0)
button.bind('<Enter>', run)

root.mainloop()