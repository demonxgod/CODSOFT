import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

def add_task():
    task = task_field.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        the_cursor.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
        the_connection.commit()
        task_field.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        task = task_listbox.get(index)
        the_cursor.execute("DELETE FROM tasks WHERE title=?", (task,))
        the_connection.commit()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete!")

def delete_all_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)
        the_cursor.execute("DELETE FROM tasks")
        the_connection.commit()

def close():
    if messagebox.askokcancel("Confirmation", "Are you sure you want to exit?"):
        guiWindow.destroy()

def retrieve_database():
    the_cursor.execute("SELECT title FROM tasks")
    for row in the_cursor.fetchall():
        task_listbox.insert(tk.END, row[0])

def list_update():
    task_listbox.delete(0, tk.END)
    retrieve_database()

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager - DAILYWORK")
    guiWindow.geometry("500x500+750+200")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#F0F0F0") 

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    header_frame = tk.Frame(guiWindow, bg="#00796B")  
    functions_frame = tk.Frame(guiWindow, bg="#80CBC4") 
    listbox_frame = tk.Frame(guiWindow, bg="#B2DFDB") 

    header_frame.pack(fill="x")
    functions_frame.pack(side="left", expand=True, fill="y", padx=5, pady=5) 
    listbox_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)  

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Arial", 24),   
        background="#00796B",  
        foreground="#FFFFFF"  
    )
    header_label.pack(pady=10) 

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Arial", 12, "bold"),  
        background="#80CBC4",  
        foreground="#004D40"  
    )
    task_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  

    task_field = ttk.Entry(
        functions_frame,
        font=("Arial", 12),
        width=25,
        background="#FFFFFF",  
        foreground="#000000"  
    )
    task_field.grid(row=1, column=0, padx=10, pady=5, sticky="w")  
    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=20,
        command=add_task
    )
    add_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")  

    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=20,
        command=delete_task
    )
    del_button.grid(row=3, column=0, padx=10, pady=5, sticky="w")  

    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=20,
        command=delete_all_tasks
    )
    del_all_button.grid(row=4, column=0, padx=10, pady=5, sticky="w") 
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=20,
        command=close
    )
    exit_button.grid(row=5, column=0, padx=10, pady=5, sticky="w") 
    task_listbox = tk.Listbox(
        listbox_frame,
        width=35,
        height=15,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#80CBC4", 
        selectforeground="#FFFFFF"  
    )
    task_listbox.pack(padx=10, pady=10, fill="both", expand=True)  

    retrieve_database()
    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()
