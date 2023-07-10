#!/usr/bin/python3
""" 12. My integer """


class MyInt(int):
    """
    a class MyInt that inherits from int
    """
    def __eq__(self, value):
        """ invert equal """
        return self.real != value

    def __ne__(self, value):
        """ invert notequal """
        return self.real == value
