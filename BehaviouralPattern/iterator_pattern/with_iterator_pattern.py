from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Book:
    def __init__(self, book_name):
        self.name = book_name

class BookCollection:
    def __init__(self):
        self.book_collection = []

    def add_book(self, book: Book):
        self.book_collection.append(book)

    def get_books(self):
        return self.book_collection
    
    # Inner class
    class BookIterator(Iterator):
        def __init__(self, books: list[Book]):
            self.__books = books
            self.__position = 0

        def has_next(self):
            return self.__position < len(self.__books)
        
        def next(self):
            if self.has_next():
                book = self.__books[self.__position]
                self.__position += 1
                return book
            else:
                raise StopIteration
        
    def create_iterator(self):
        return self.BookIterator(self.book_collection)
    

class Client:
    def main(self):
        book_collection = BookCollection()

        book_collection.add_book(Book('C++ Book'))
        book_collection.add_book(Book('Python Book'))
        book_collection.add_book(Book('Java Book'))

        iterator = book_collection.create_iterator()
        while iterator.has_next():
            book = iterator.next()
            print(book.name)

if __name__ == "__main__":
    Client().main()