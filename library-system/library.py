
class Shelf:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.list_contents = []

    def add_book(self, book):
        self.list_contents.append(book.title)

    def display_content(self):
        print(f"[{self.name} OVERVIEW]")
        print(f"Available: {self.list_contents}")

class Library:
    def __init__(self, room) -> None:
        self.room = room
        self.librarian = None
        self.list_of_shelves = []

    def add_librarian(self, librarian):
        self.librarian = librarian

    def add_shelf(self, shelf: Shelf):
        self.list_of_shelves.append(shelf)

    def display_shelf(self):
        pass
        