# ============================================
# To-Do List (GUI Version)
# Author: Saloni Tiwari
# Topic: Tkinter + File Handling
# ============================================

import tkinter as tk
from tkinter import messagebox
from task_storage import load_tasks, save_tasks

# ========================================
# Functions
# ========================================
def add_task():
    title = entry.get().strip()

    if not title:
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    tasks.append({"title": title, "status": "Pending", "category": "Work"})
    save_tasks(tasks)
    entry.delete(0, tk.END)
    view_tasks()
    messagebox.showinfo("Success", "Task added!")

def view_tasks():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks, start=1):
        listbox.insert(tk.END, f"{i}. [{t['status']}] {t['title']} ({t['category']})")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        removed = tasks.pop(selected)
        save_tasks(tasks)
        view_tasks()
        messagebox.showinfo("Deleted", f"Task '{removed['title']}' deleted!")
    except:
        messagebox.showerror("Error", "Select a task to delete!")


# ========================================
# GUI Setup
# ========================================
tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

tk.Label(root, text="To-Do List", font=("Arial", 14, "bold")).pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="View Tasks", command=view_tasks).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=40, height=10, yscrollcommand=scroll.set)
listbox.pack()

scroll.config(command=listbox.yview)

# Load initial tasks
view_tasks()

# Run
root.mainloop()