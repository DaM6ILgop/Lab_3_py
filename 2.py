class Book:
    code_counter = 1

    def __init__(self, author, title):
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.author = author
        self.title = title
        self.code = Book.code_counter
        Book.code_counter += 1

    def tag(self):
        return [word for word in self.title.split() if word[0].isupper()]


class Library:
    def __init__(self, number, address):
        self.number = number
        self.address = address
        self.books = []

    def __iadd__(self, book):
        self.books.append(book)
        return self

    def __iter__(self):
        return iter(self.books)


lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')

for book in lib:
    print(f"[{book.code}] {book.author} '{book.title}'")
    print(book.tag())