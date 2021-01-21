import tkinter as tk
after_id = None
status='Start'
s=0
def run():
    global after_id
    global s
    s+=1
    timer.config(text=str(s))
    after_id = root.after(1000, run)

def startStop():
    global status
    global after_id
    global s
    if status == 'Start':
        status = 'Stop'
        btn.config(text=status)
        s=-1
        run()
    elif status == 'Stop':
        status = 'Start'
        btn.config(text=status)
        root.after_cancel(after_id)


root = tk.Tk()
root.title('Clicker')
root.geometry('+700+200')

btn = tk.Button(root, text='Start', command=startStop)
timer = tk.Label(root, text='0', )

timer.pack()
btn.pack()
root.mainloop()