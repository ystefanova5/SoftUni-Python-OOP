from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if book in self.books:
            return f"The book {book.title} is already in the Library"
        self.books.append(book)

    def remove_book(self, title):
        try:
            book = self.find_book(title)
            self.books.remove(book)
        except ValueError:
            return f"The book {title} is not in the Library"

        return f"The book {title} by {book.author} was removed from the Library"

    def find_book(self, title):
        try:
            book = next(filter(lambda x: x.title == title, self.books))
        except StopIteration:
            return "Book not found"

        return book


library = Library()
for number in range(1, 11):
    book = Book(f"Title {number}", f"Author {number}")
    library.add_book(book)

test_book = library.find_book("Title 3")
print(library.add_book(test_book))
print(library.remove_book("Title 3"))
print(library.remove_book("Title 3"))
book_2 = library.find_book("Title 2")
print(library.find_book("Title 3"))
print(book_2.title)
print(book_2)
