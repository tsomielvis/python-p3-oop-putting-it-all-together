#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # This will use the property setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise ValueError('page_count must be an integer')
        self._page_count = value

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')

book = Book("Book", 25)
try:
    book.page_count = '2'  # This will raise an error
except ValueError as e:
    print(e)

print(book.page_count)
book.turn_page()
