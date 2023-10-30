from person import Student, Librarian
from article import Book, Newspaper, Magazine, Research_Paper
from library import Library, Shelf


if __name__ == '__main__':
    # create librarian and library
    librarian = Librarian('0001', 'Mary', 20)
    library = Library('CB 302')
    library.add_librarian(librarian)

    # create shelf and add to library
    shelf_1 = Shelf('0001', 'Book Shelf')
    library.add_shelf(shelf_1)

    # create books, newspaper, magazines, and research papers
    book_1 = Book('0001', 'Introduction to Programming', 'John Flinch', 'ABC Publishing', '09/23/2022')

    # add books to the shelf
    shelf_1.add_book(book_1)

    # create student
    student_1 = Student('0001', 'Michael', 19, 'BSCS')

    # borrow
    student_1.borrow_book(book_1, shelf_1)

    # display
    student_1.display()

    shelf_1.display_content()