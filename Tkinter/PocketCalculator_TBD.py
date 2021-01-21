import tkinter as tk

gui = tk.Tk()
gui.title('Calculator'.center(20))
gui.minsize(277,250)
gui.geometry('+600+300')

entry_field = tk.Entry(gui, width=45)
entry_field.grid(row=0, column=0)




btn_7 = tk.Button(gui, text = '7')
btn_8 = tk.Button(gui, text = '8')
btn_9 = tk.Button(gui, text = '9')
btn_4 = tk.Button(gui, text = '4')
btn_5 = tk.Button(gui, text = '5')
btn_6 = tk.Button(gui, text = '6')
btn_1 = tk.Button(gui, text = '1')
btn_2 = tk.Button(gui, text = '2')
btn_3 = tk.Button(gui, text = '3')
btn_0 = tk.Button(gui, text = '0')
btn_C = tk.Button(gui, text = 'C')
btn_point = tk.Button(gui, text = '.')

btn_add = tk.Button(gui, text = '+')
btn_minus = tk.Button(gui, text = '-')

btn_equal = tk.Button(gui, text = '=')
btn_multiply = tk.Button(gui, text = '*')
btn_0 = tk.Button(gui, text = '+/-')
btn_divide = tk.Button(gui, text = '/')
gui.mainloop()

