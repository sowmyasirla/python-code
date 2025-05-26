class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def status(self):
        return "Available" if self.available else "Not Available"


# Sample book inventory
library = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

# Menu loop
def show_menu():
    print("\nLibrary Menu")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nAvailable Books:")
        for i, book in enumerate(library):
            print(f"{i+1}. {book.title} by {book.author} - {book.status()}")

    elif choice == "2":
        index = int(input("Enter book number to borrow: ")) - 1
        if 0 <= index < len(library):
            library[index].borrow()
        else:
            print("Invalid book number.")

    elif choice == "3":
        index = int(input("Enter book number to return: ")) - 1
        if 0 <= index < len(library):
            library[index].return_book()
        else:
            print("Invalid book number.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")