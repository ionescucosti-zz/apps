import tkinter as tk

root = tk.Tk()
root.title('Crono')
root.geometry('+700+200')

label = tk.Label(root, text='0')
#label.after(5,start)
label.pack()

seconds = -1
def start(n=10):
    #time.sleep(1)
    global seconds
    seconds+=1
    label.configure(text='%i' %seconds)

btn = tk.Button(root, text='start', command=start)
btn.after(5, start)
btn.pack()

root.mainloop()
