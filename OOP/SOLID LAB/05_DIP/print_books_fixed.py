class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter(Formatter):
    def format(self, book: Book):
        return book.content[:4]


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


base_formatter = Formatter()
paper_formatter = PaperFormatter()
book = Book("Some text")

p = Printer()

p.get_book(book, base_formatter)
p.get_book(book, paper_formatter)