import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

'''consider workflow: 
        1) create the widget widget = SomeWidget(parent)
        2) Add the widget to parent structure if needed: notebook.add(create_set_frame)
        3) Display it with geometry manager -
        
    Note: .add() is only used for special container widgets like ttk.Notebook (tabbed interfaces)
    tk.PanedWindow (Resizable panes), tk.Menu (menu items). They have special behavior beyond just displaying children. 
        
        '''

if __name__=="__main__": 
    root = tk.Tk()
    root.title("Flashcards App")
    root.geometry("500x400")

    #Apply Styling 
    style = Style(theme="superhero")
    style.configure("TLabel", font=("TkDefaultFont", 18))
    style.configure("TButton", font=("TkDefaultFont", 14))

    # Set variables for storing user input
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    #create a notebook widget to manage tabs?
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True) #geometry manager; makes appear; 

    #create set tab and content
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text="Create Set") #establishes create_set_frame as a child of notebook

    #Label and Entry Widgets for entering name, word, and definition
    set_label = ttk.Label(create_set_frame, text="Set Name").pack(padx=5, pady=5)
    term = ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)
   
    term_label = ttk.Label(term, text="Term").pack(padx=5, pady=5)

    definition = ttk.Entry(create_set_frame).pack(padx=5, pady=5)
    term_label = ttk.Label(definition, text="Definition").pack(padx=5, pady=5)


    





    root.mainloop()