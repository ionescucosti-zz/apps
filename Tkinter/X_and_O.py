import tkinter as tk
from functools import partial
from random import randint
from tkinter import messagebox

buttons = []
unmarked = {}
over = None

def user_mark():
    global unmarked
    global bname
    global turn
    bname.config(text='O') # se modifica textul butonului
    #btn.configure(font="10 bold")
    bname['state'] = tk.DISABLED # se dezactiveaza
    unmarked.pop(bname)   #sterge dinn unmarked
    return check_lines()

def computer_mark():
    global unmarked
    global turn
    inx = randint(0,len(unmarked.keys())-1)
    btn = list(unmarked.keys())[inx]
    btn.config(text='X') # seteaza textul
    btn.configure(font = "10 bold")
    btn['state'] = tk.DISABLED # il dezactiveaza
    unmarked.pop(btn)  # sterge dinn unmarked
    return check_lines()

def check_lines():
    state =['O','X']
    global over
    for i in state:
        if buttons[0].cget('text') == buttons[1].cget('text') == buttons[2].cget('text') == i:
            over = [True, i]
        elif buttons[3].cget('text') == buttons[4].cget('text') == buttons[5].cget('text') == i:
            over = [True, i]
        elif buttons[6].cget('text') == buttons[7].cget('text') == buttons[8].cget('text') == i:
            over = [True, i]
        elif buttons[0].cget('text') == buttons[3].cget('text') == buttons[6].cget('text') == i:
            over = [True, i]
        elif buttons[1].cget('text') == buttons[4].cget('text') == buttons[7].cget('text') == i:
            over = [True, i]
        elif buttons[2].cget('text') == buttons[5].cget('text') == buttons[8].cget('text') == i:
            over = [True, i]
        elif buttons[0].cget('text') == buttons[4].cget('text') == buttons[8].cget('text') == i:
            over = [True, i]
        elif buttons[6].cget('text') == buttons[4].cget('text') == buttons[2].cget('text') == i:
            over = [True, i]

def start(n):
    global bname
    global over
    bname = (buttons[n]) #n=buton , se defineste butonul global

    if over is not None and over[0] is True:
        if over[1]=='O':
            messagebox.showinfo('Game Over!','You won!')
        elif over[1]=='X':
            messagebox.showinfo('Game Over!','Computer won!')
    else:
        user_mark()
        if over is not None and over[0] is True:
            if over[1] == 'O':
                messagebox.showinfo('Game Over!', 'You won!')
            elif over[1] == 'X':
                messagebox.showinfo('Game Over!', 'Computer won!')
        else:
            computer_mark()

wnd = tk.Tk()
wnd.title("TicTacToe")
wnd.geometry('+700+200')

for x in range(3):  # Buttons
    for y in range(3):
        btn = tk.Button(wnd, text='', width=12, height=5)
        btn.grid(row=x, column=y)
        buttons.append(btn)

for i in buttons:
    i.config(command=partial(start, buttons.index(i)))
    unmarked[i] = buttons.index(i)

buttons[4].config(text='X')
#buttons[4].configure(font = "10 bold")
buttons[4]['state'] = tk.DISABLED
unmarked.pop(list(unmarked.keys())[4])

wnd.mainloop()
