class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Books in Library:")
            for book in self.books:
                print("-", book)

library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Artificial Intelligence")

library.display_books()
