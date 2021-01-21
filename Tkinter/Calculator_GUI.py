import  tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Calculator'.center(20))
window.minsize(300,130)
window.geometry('+600+300')

def Click():
    switch.set()

def Calculate():
    ev1 = entry1.get()
    ev2 = entry2.get()
    if len(ev1)<1:
        messagebox.showinfo("Result", 'Left side empty!')
    elif len(ev2)<1:
        messagebox.showinfo("Result", 'Right side empty!')
    elif not ev1.isdigit():
        messagebox.showinfo("Result", 'Left side not a number!')
    elif not ev2.isdigit():
        messagebox.showinfo("Result", 'Left side empty!')
    else:
        try:
            if isinstance(ev1,float) or isinstance(ev2, float):
                if switch.get() == 1:
                    messagebox.showinfo("Result", float(ev1) + float(ev2))
                elif switch.get() == 2:
                    messagebox.showinfo("Result", float(ev1) - float(ev2))
                elif switch.get() == 3:
                    messagebox.showinfo("Result", float(ev1) * float(ev2))
                elif switch.get() == 4:
                    messagebox.showinfo("Result", float(ev1) / float(ev2))
            else:
                if switch.get() == 1:
                    messagebox.showinfo("Result", int(ev1) + int(ev2))
                elif switch.get() == 2:
                    messagebox.showinfo("Result", int(ev1) - int(ev2))
                elif switch.get() == 3:
                    messagebox.showinfo("Result", int(ev1) * int(ev2))
                elif switch.get() == 4:
                    messagebox.showinfo("Result", int(ev1)/int(ev2))
        except ZeroDivisionError:
            messagebox.showinfo("Result", 'Zero division impossible!')
        except Exception as e:
            messagebox.showinfo("Result", 'Error: '+e)

buttons = [('+',1),('-',2),('*',3),('/',4)]
switch = tk.IntVar()
switch.set(1)

for i in buttons:
    tk.Radiobutton(window,text=i[0], variable = switch, command = Click, value=i[1])\
        .grid(row=buttons.index(i), column=1)

entry1 = tk.Entry(window, width=20)
entry2 = tk.Entry(window, width=20)
entry1.grid(row=1, column=0, rowspan=2)
entry2.grid(row=1, column= 2, rowspan=2)

button_Evaluate = tk.Button(window, text="Evaluate", command=Calculate).grid(row=4, column=1)

window.mainloop()