#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Week 1 IS 211 Assignment - Part 2"""


class Book(object):
    """Creates a book"""

    author = ''
    title = ''

    def __init__(self, author, title):
        """Constructor for book.
            Args:
                author: name of author
                title: name of book
            Attributes:
                author: name of author
                title: name of book
        """
        self.author = author
        self.title = title

    def display(self):
        """Displays a book's title and author."""
        print "{}, written by {}".format(self.title, self.author)

B1 = Book('John Steinbeck', 'Of Mice and Men')
B2 = Book('Harper Lee', 'To Kill A Mockingbird')

B1.display()
B2.display()
