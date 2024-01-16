import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Null input is invalid,please enter a task")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Null selection is invalid,please select a task to delete")

app = tk.Tk()
app.title("To-Do List")


frame_tasks = tk.Frame(app)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, selectbackground="grey")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(app, width=40,bg="yellow")
entry_task.pack(pady=10)

button_add = tk.Button(app, text="Add Task", width=20, command=add_task,bg="green")
button_add.pack(pady=5)

button_delete = tk.Button(app, text="Delete Task", width=20, command=delete_task,bg="red")
button_delete.pack(pady=5)


app.mainloop()
