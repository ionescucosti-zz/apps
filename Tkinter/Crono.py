import tkinter as tk

root = tk.Tk()
root.title('Crono')
root.geometry('+700+200')

s=-1
def start():
    global s
    s+=1
    label['text'] = str(s)
    label.after(1000,start)

label = tk.Label(root, text='0')
label.after_cancel(10)
label.pack()

btn = tk.Button(root, text='Start', command=start).pack()
root.mainloop()