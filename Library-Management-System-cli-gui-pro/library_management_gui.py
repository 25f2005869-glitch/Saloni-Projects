
========================================
Library Management System (GUI + OOP)

Author: Saloni Tiwari
Topic: OOP + Tkinter + File Handling
Description:
GUI based library system with:
- Add Book
- View Books
- Search Book
- Delete Book
========================================

import tkinter as tk
from tkinter import messagebox

# ========================================
# Library Class (OOP)
# ========================================
class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = self.load_books()

    def _norm(self, s: str) -> str:
        return s.strip().lower()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                f.write(book + "\n")

    def add_book(self, book):
        book = book.strip()
        if not book:
            return False

        existing = {self._norm(b) for b in self.books}
        if self._norm(book) in existing:
            return False

        self.books.append(book)
        self.save_books()
        return True

    def delete_book(self, book):
        key = self._norm(book)
        for i, b in enumerate(self.books):
            if self._norm(b) == key:
                self.books.pop(i)
                self.save_books()
                return True
        return False

    def search_book(self, book):
        key = self._norm(book)
        return any(self._norm(b) == key for b in self.books)


# ========================================
# GUI Class
# ========================================
class LibraryGUI:
    def __init__(self, root):
        self.lib = Library()

        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x400")

        tk.Label(root, text="Author: Saloni Tiwari").pack(pady=5)

        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book).pack(pady=5)
        tk.Button(root, text="View Books", command=self.view_books).pack(pady=5)
        tk.Button(root, text="Search Book", command=self.search_book).pack(pady=5)
        tk.Button(root, text="Delete Book", command=self.delete_book).pack(pady=5)

        # Listbox
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack(pady=10)

    def add_book(self):
        book = self.entry.get().strip()
        if self.lib.add_book(book):
            messagebox.showinfo("Success", "Book Added!")
            self.entry.delete(0, tk.END)
            self.view_books()
        else:
            messagebox.showerror("Error", "Invalid or Duplicate Book!")

    def view_books(self):
        self.listbox.delete(0, tk.END)
        for book in self.lib.books:
            self.listbox.insert(tk.END, book)

    def search_book(self):
        book = self.entry.get().strip()
        if not book:
            messagebox.showerror("Error", "Book name cannot be empty!")
            return

        if self.lib.search_book(book):
            messagebox.showinfo("Result", "Book Found!")
        else:
            messagebox.showerror("Result", "Book Not Found!")

    def delete_book(self):
        book = self.entry.get().strip()
        if not book:
            messagebox.showerror("Error", "Book name cannot be empty!")
            return

        if self.lib.delete_book(book):
            messagebox.showinfo("Success", "Book Deleted!")
            self.view_books()
        else:
            messagebox.showerror("Error", "Book Not Found!")


# ========================================
# Run Application
# ========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
