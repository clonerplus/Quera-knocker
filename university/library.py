import gc


class Book:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class Library:
    def __init__(self):
        self.book_count = 0
        self.left_book = None
        self.right_book = None

    def add_left(self, name):
        new_book = Book(name)
        new_book.right = self.left_book
        if self.left_book:
            self.left_book.left = new_book
        self.left_book = new_book
        if self.right_book is None:
            self.right_book = new_book
        self.book_count += 1

    def add_right(self, name):
        new_book = Book(name)
        new_book.left = self.right_book
        if self.right_book:
            self.right_book.right = new_book
        self.right_book = new_book
        if self.left_book is None:
            self.left_book = new_book
        self.book_count += 1

    def delete_left(self):
        self.left_book = self.left_book.right
        self.book_count -= 1
        gc.collect()

    def print_library(self):
        book = self.left_book
        while book is not None:
            print(book.name)
            book = book.right


if __name__ == "__main__":
    n = int(input())
    Library = Library()

    for i in range(n):
        Library.add_right(input())
    # Library.print_library()

    while True:
        com = input()
        if com == "AddLeft":
            Library.add_left(input())
        elif com == "AddRight":
            Library.add_right(input())
        elif com == "DeleteLeft":
            Library.delete_left()
        else:
            print(Library.book_count)
            Library.print_library()
            exit(0)

