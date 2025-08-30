class Book:
    def __init__(self, book_name):
        self.name = book_name


class BookCollection:
    def __init__(self):
        # Could be a list, set, dict, database cursor, anything
        self.book_collection = []

    def add_book(self, book: Book):
        self.book_collection.append(book)

    def __iter__(self):
         # The iterator works regardless of data type
        for book in self.book_collection:
            yield book   # <-- This replaces BookIterator


class Client:
    def main(self):
        book_collection = BookCollection()
        book_collection.add_book(Book('C++ Book'))
        book_collection.add_book(Book('Python Book'))
        book_collection.add_book(Book('Java Book'))

        # Iteration works directly
        for book in book_collection:
            print(book.name)


if __name__ == "__main__":
    Client().main()
