class Book:
    def __init__(self, book_name):
        self.name = book_name

class BookCollection:
    def __init__(self):
        self.book_collection = list()

    def add_book(self, book: Book):
        self.book_collection.append(book)

    def get_book(self):
        return self.book_collection
    

class Client:
    def main(self):
        # Initilaise book collection
        book_collection: BookCollection = BookCollection()

        # Add books
        book_collection.add_book(Book('C++ Book'))
        book_collection.add_book(Book('Python Book'))
        book_collection.add_book(Book('Java Book'))

        # Iterate the books
        for book in book_collection.get_book():
            print(book.name)

if __name__ == "__main__":
    obj: Client = Client()
    obj.main()