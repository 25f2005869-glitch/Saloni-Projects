# =========================================
# Library Management System PRO (GUI)
# Author: Saloni Tiwari
# Topic: Tkinter + OOP + File Handling
# =========================================

import tkinter as tk
from tkinter import messagebox

# ========================================
# Library Class (OOP)
# ========================================
class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    title, status, category = line.strip().split("|")
                    books.append({
                        "title": title,
                        "status": status,
                        "category": category
                    })
        except FileNotFoundError:
            pass
        return books

    def save_books(self):
        with open(self.filename, "w") as f:
            for b in self.books:
                f.write(f"{b['title']}|{b['status']}|{b['category']}\n")

    def add_book(self, title, category):
        title = title.strip()
        if not title:
            return False

        for b in self.books:
            if b["title"].lower() == title.lower():
                return False

        self.books.append({
            "title": title,
            "status": "Available",
            "category": category
        })
        self.save_books()
        return True

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            self.books.pop(index)
            self.save_books()
            return True
        return False

    def issue_book(self, index):
        if self.books[index]["status"] == "Available":
            self.books[index]["status"] = "Issued"
            self.save_books()

    def return_book(self, index):
        if self.books[index]["status"] == "Issued":
            self.books[index]["status"] = "Available"
            self.save_books()

    def search_book(self, keyword):
        keyword = keyword.lower()
        return [b for b in self.books if keyword in b["title"].lower()]


# ========================================
# GUI Class
# ========================================
class LibraryGUI:
    def __init__(self, root):
        self.lib = Library()
        self.root = root
        self.root.title("Library PRO")
        self.root.geometry("500x550")

        tk.Label(root, text="Library Management PRO", font=("Arial", 16, "bold")).pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Category
        self.category_var = tk.StringVar(value="General")
        tk.OptionMenu(root, self.category_var, "General", "Science", "Novel", "Study").pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book).pack(pady=5)
        tk.Button(root, text="Delete Book", command=self.delete_book).pack(pady=5)
        tk.Button(root, text="Issue Book", command=self.issue_book).pack(pady=5)
        tk.Button(root, text="Return Book", command=self.return_book).pack(pady=5)
        tk.Button(root, text="Search", command=self.search_book).pack(pady=5)
        tk.Button(root, text="Show All", command=self.view_books).pack(pady=5)

        # Listbox
        frame = tk.Frame(root)
        frame.pack(pady=10)

        scroll = tk.Scrollbar(frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame, width=60, height=15, yscrollcommand=scroll.set)
        self.listbox.pack()

        scroll.config(command=self.listbox.yview)

        self.view_books()

    def view_books(self, books=None):
        self.listbox.delete(0, tk.END)

        if books is None:
            books = self.lib.books

        for i, b in enumerate(books):
            text = f"{i+1}. {b['title']} ({b['category']}) [{b['status']}]"

            self.listbox.insert(tk.END, text)

            if b["status"] == "Available":
                self.listbox.itemconfig(tk.END, fg="green")
            else:
                self.listbox.itemconfig(tk.END, fg="red")

    def add_book(self):
        title = self.entry.get()
        category = self.category_var.get()

        if self.lib.add_book(title, category):
            messagebox.showinfo("Success", "Book Added")
            self.entry.delete(0, tk.END)
            self.view_books()
        else:
            messagebox.showerror("Error", "Invalid or Duplicate Book")

    def delete_book(self):
        try:
            index = self.listbox.curselection()[0]
            self.lib.delete_book(index)
            self.view_books()
        except:
            messagebox.showerror("Error", "Select a book")

    def issue_book(self):
        try:
            index = self.listbox.curselection()[0]
            self.lib.issue_book(index)
            self.view_books()
        except:
            messagebox.showerror("Error", "Select a book")

    def return_book(self):
        try:
            index = self.listbox.curselection()[0]
            self.lib.return_book(index)
            self.view_books()
        except:
            messagebox.showerror("Error", "Select a book")

    def search_book(self):
        keyword = self.entry.get()
        results = self.lib.search_book(keyword)
        self.view_books(results)


# ========================================
# Run
# ========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()