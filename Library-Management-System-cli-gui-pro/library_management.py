# Load books from file at start
try:
    with open("books.txt", "r") as file:
        books = file.read().splitlines()
except FileNotFoundError:
    books = []

def normalize(title: str) -> str:
    return title.strip().lower()

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # Add Book
    if choice == "1":
        book_name = input("Enter book name: ").strip()

        if not book_name:
            print("Book name cannot be empty!")
            continue

        existing = {normalize(b) for b in books}
        if normalize(book_name) in existing:
            print("This book already exists!")
            continue

        books.append(book_name)

        with open("books.txt", "a") as file:
            file.write(book_name + "\n")

        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if books:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)
        else:
            print("No books available.")

    # Search Book (case-insensitive)
    elif choice == "3":
        search = input("Enter book name to search: ").strip()
        if not search:
            print("Book name cannot be empty!")
            continue

        found = any(normalize(b) == normalize(search) for b in books)
        if found:
            print("Book found!")
        else:
            print("Book not found.")

    # Delete Book (case-insensitive)
    elif choice == "4":
        delete_book = input("Enter book name to delete: ").strip()
        if not delete_book:
            print("Book name cannot be empty!")
            continue

        idx = next((i for i, b in enumerate(books) if normalize(b) == normalize(delete_book)), None)
        if idx is not None:
            books.pop(idx)

            # Rewrite file after delete
            with open("books.txt", "w") as file:
                for book in books:
                    file.write(book + "\n")

            print("Book deleted successfully!")
        else:
            print("Book not found.")

    # Exit
    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.")
