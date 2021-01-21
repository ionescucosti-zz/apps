import tkinter

import winsound

FREQ = 2500
DUR = 150

after_id = None
secs = 0

def beeper():
    global after_id
    global secs
    secs += 1
    winsound.Beep(FREQ, DUR)
    timer.config(text=str(secs))
    after_id = top.after(1000, beeper)

def start():
    global secs
    secs = 0
    beeper()  # start repeated checking

def stop():
    global after_id
    if after_id:
        top.after_cancel(after_id)
        after_id = None

top = tkinter.Tk()
top.title('MapAwareness')
top.geometry('200x100')

timer = tkinter.Label(top, text='0', )

startButton = tkinter.Button(top, height=2, width=20, text="Start",
                             command=start)
stopButton = tkinter.Button(top, height=2, width=20, text="Stop",
                            command=stop)
timer.pack()
startButton.pack()
stopButton.pack()
top.mainloop()