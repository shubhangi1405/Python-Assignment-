# Experiment 6: Library Class

class Library:
    books = []  # Class variable to hold all books

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True
        Library.books.append(self)

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f'Book "{self.book_name}" checked out successfully.')
        else:
            print(f'Sorry, "{self.book_name}" is currently unavailable.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'Book "{self.book_name}" returned successfully.')
        else:
            print(f'"{self.book_name}" was not checked out.')

    @classmethod
    def display_available(cls):
        available = [b for b in cls.books if b.is_available]
        if available:
            print('\n--- Available Books ---')
            for b in available:
                print(f'  Title: {b.book_name:30s} | Author: {b.author}')
        else:
            print('No books are currently available.')

# Main Program
b1 = Library('Python Crash Course', 'Eric Matthes')
b2 = Library('Clean Code', 'Robert C. Martin')
b3 = Library('The Pragmatic Programmer', 'Hunt & Thomas')
b4 = Library('Introduction to Algorithms', 'Cormen et al.')

Library.display_available()

b1.check_out()
b3.check_out()
b1.check_out()  # Try again

Library.display_available()

b1.return_book()
