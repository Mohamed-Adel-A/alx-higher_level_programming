#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ class MyList that inherits from list """

    def __init__(self):
        """ init mylist """
        super().__init__()

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
