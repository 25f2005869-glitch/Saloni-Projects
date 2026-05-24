# ============================================
# To-Do List PRO (GUI)
# Author: Saloni Tiwari
# Topic: Tkinter + File Handling + Status
# ============================================

import tkinter as tk
from tkinter import messagebox
from task_storage import load_tasks, save_tasks

# ========================================
# Functions
# ========================================
def add_task():
    title = entry.get().strip()
    category = category_var.get()

    if not title:
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    task = {"title": title, "status": "Pending", "category": category}
    tasks.append(task)

    save_tasks(tasks)
    entry.delete(0, tk.END)
    view_tasks()

def view_tasks():
    listbox.delete(0, tk.END)

    for t in tasks:
        text = f"[{t['status']}] {t['title']} ({t['category']})"

        if t["status"] == "Done":
            listbox.insert(tk.END, text)
            listbox.itemconfig(tk.END, fg="green")
        else:
            listbox.insert(tk.END, text)
            listbox.itemconfig(tk.END, fg="red")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["status"] = "Done"
        save_tasks(tasks)
        view_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks(tasks)
        view_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

# ========================================
# GUI Setup
# ========================================
tasks = load_tasks()

root = tk.Tk()
root.title("To-Do PRO")
root.geometry("450x500")

tk.Label(root, text="To-Do List PRO", font=("Arial", 16, "bold")).pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Category Dropdown
category_var = tk.StringVar(value="Work")
tk.OptionMenu(root, category_var, "Work", "Study", "Personal").pack()

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Listbox
frame = tk.Frame(root)
frame.pack(pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=50, height=12, yscrollcommand=scroll.set)
listbox.pack()

scroll.config(command=listbox.yview)

# Load tasks
view_tasks()

# Run
root.mainloop()