from tkinter import *
from tkinter import ttk
# root = Tk()
# l =ttk.Label(root, text="Starting...")
# l.grid()

# # bind command (EVENT, FUNCTION)
# l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# l.bind('<3>', lambda e: l.configure(text='Clicked third mouse button'))
# l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# l.bind('<B3-Motion>', lambda e: l.configure(text=f'third button drag to {e.x},{e.y}'))
# root.mainloop()

root = Tk() #this instantiates the main window "root"

'''This is the container frame. It will organize space and contain the other widgets'''
content = ttk.Frame(root) 

'''This creates another frame inside of content'''
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one_button = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two_button = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three_button = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok_button = ttk.Button(content, text="Okay")
cancel_button = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=5, rowspan=5)
namelbl.grid(column=0, row=0)
name.grid(column=1, row=0)
one_button.grid(column=0, row=5, padx=(10))
two_button.grid(column=1, row=5, padx=(10))
three_button.grid(column=2, row=5, padx=(10))
ok_button.grid(column=3, row=5)
cancel_button.grid(column=4, row=5)


root.mainloop()
