class Article:
    def __init__(self, id, title, author, publisher, publishing_date) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publishing_date = publishing_date

class Book(Article):
    def __init__(self, id, title, author, publisher, publishing_date) -> None:
        super().__init__(id, title, author, publisher, publishing_date)

class Newspaper(Article):
    def __init__(self, id, title, author, publisher, publishing_date) -> None:
        super().__init__(id, title, author, publisher, publishing_date)

class Magazine(Article):
    def __init__(self, id, title, author, publisher, publishing_date) -> None:
        super().__init__(id, title, author, publisher, publishing_date)

class Research_Paper(Article):
    def __init__(self, id, title, author, publisher, publishing_date) -> None:
        super().__init__(id, title, author, publisher, publishing_date)
