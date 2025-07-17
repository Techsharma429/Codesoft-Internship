import tkinter as tk
from tkinter import messagebox

#  store the tasks
tasks = []
#Add task function
def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(task_list_frame, text=task_text, variable=var, font=('Arial', 14), anchor='w')
        checkbox.pack(fill=tk.X, padx=20, pady=2)
        tasks.append((checkbox, var))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

#  mark the task  done (add ✓)
def mark_done():
    for cb, var in tasks:
        if var.get() == 1 and not cb.cget("text").startswith("✓ "):
            cb.config(text="✓ " + cb.cget("text"))
            var.set(0)

#  Delete selected tasks
def delete_task():
    global tasks
    new_tasks = []
    for cb, var in tasks:
        if var.get() == 1:
            cb.destroy()
        else:
            new_tasks.append((cb, var))
    tasks = new_tasks

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.attributes("-fullscreen", True)  # Full screen

# Exit fullscreen by  Esc
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

#  input area
top_frame = tk.Frame(root, pady=20)
top_frame.pack()

label = tk.Label(top_frame, text="Enter your task:", font=('Arial', 14))
label.grid(row=0, column=0, padx=10)

task_entry = tk.Entry(top_frame, width=50, font=('Arial', 14))
task_entry.grid(row=0, column=1, padx=10)

add_button = tk.Button(top_frame, text="Add Task", font=('Arial', 12), command=add_task)
add_button.grid(row=0, column=2, padx=10)

mark_button = tk.Button(top_frame, text="Mark as Done", font=('Arial', 12), command=mark_done)
mark_button.grid(row=0, column=3, padx=10)

delete_button = tk.Button(top_frame, text="Delete Task", font=('Arial', 12), command=delete_task)
delete_button.grid(row=0, column=4, padx=10)

# Task list box
task_list_frame = tk.Frame(root)
task_list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

#Run the TO-DO List
root.mainloop()

