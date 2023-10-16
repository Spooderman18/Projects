import tkinter as tk

def add_task(): #used to add a task
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task(): #used to remove selected task
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_complete(): #changes the background color when a task is marked complete
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_listbox.itemconfig(task_index,{'bg':'green'})

app=tk.Tk() #opens the application
app.title("to-do list")

task_entry = tk.Entry(app, width=30)
add_button = tk.Button(app, text="Add Task", command=add_task) #button for adding a task
remove_button = tk.Button(app, text="Remove Task", command=remove_task) #button for removing a task
complete_button = tk.Button(app, text="Mark Complete", command=mark_complete)

task_listbox = tk.Listbox(app, width=30, height=30) #creates a listbox for displaying of tasks 
remove_button = tk.Button(app, text="Remove Task", command=remove_task)

task_entry.grid(row=0, column=0, padx=12, pady=14)
add_button.grid(row=0, column=1, padx=12, pady=14)
task_listbox.grid(row=1, column=0, columnspan=2, padx=12, pady=14)
remove_button.grid(row=2, column=0, columnspan=2, padx=12, pady=14)
complete_button.grid(row=3, column=0, columnspan=2, padx=12, pady=14)

app.mainloop()
