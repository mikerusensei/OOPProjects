class Person:
    def __init__(self, id, name, age) -> None:
        self.id = id
        self.name = name
        self.age = age

class Librarian(Person):
    def __init__(self, id, name, age) -> None:
        super().__init__(id, name, age)
        self.returned_list = []

    def return_to_shelf(self):
        pass

class Student(Person):
    def __init__(self, id, name, age, course) -> None:
        super().__init__(id, name, age)
        self.course = course
        self.borrowed_list = []

    def borrow_book(self, book, shelf):
        self.borrowed_list.append(book.title)
        shelf.list_contents.remove(book.title)
    
    def return_book(self, book, librarian: Librarian):
        self.borrowed_list.remove(book.title)
        librarian.returned_list.append(book.title)

    def display(self):
        print(f'[STUDENT OVERVIEW]')
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Borrowed: {self.borrowed_list}")


