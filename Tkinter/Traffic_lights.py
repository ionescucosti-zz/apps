from tkinter import Tk, Button, Canvas

status = 0
phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

colours = ('red', 'yellow', 'green')

def read_status():
    for i in range(len(phases[status])):
        if i == 0:
            if phases[status][i] == True:
                canvas.itemconfig(l1,fill='red')
            elif phases[status][i] == False:
                canvas.itemconfig(l1,fill='grey')
        elif i == 1:
            if phases[status][i] == True:
                canvas.itemconfig(l2,fill='yellow')
            elif phases[status][i] == False:
                canvas.itemconfig(l2,fill='grey')
        elif i == 2:
            if phases[status][i] == True:
                canvas.itemconfig(l3, fill='green')
            elif phases[status][i] == False:
                canvas.itemconfig(l3,fill='grey')

def change():
    global status
    if status == len(phases):
        status = 0
        read_status()
        status += 1
    else:
        read_status()
        status+=1

root = Tk()              # Main window
root.title('Traffic Lights')
root.geometry('+500+200')

canvas = Canvas(root,width=100, height=240, bg='dim grey')

l1 = canvas.create_oval(15, 5, 85, 75, outline='black', width=3, fill='grey')
l2 = canvas.create_oval(15, 85, 85, 155, outline='black', width=3, fill='yellow' )
l3 = canvas.create_oval(15, 165, 85, 235, outline='black', width=3, fill='grey')

next = Button(root, text='Next', command = change)
quit = Button(root, text='Quit', command = root.destroy)

canvas.grid(row=0, padx=8, pady=8)
next.grid(row=1)
quit.grid(row=2, pady=(0,8))
root.mainloop()