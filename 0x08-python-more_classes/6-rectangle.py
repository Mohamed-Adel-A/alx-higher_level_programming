#!/usr/bin/python3
""" define classe rectangel """


class Rectangle:
    """ rectangel class """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ init the class """
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area """
        return (self.width * self.height)

    def perimeter(self):
        """ return perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """ __str___ """
        str = ""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            for i in range(self.height):
                for j in range(self.width):
                    str += "#"
                if i != self.height - 1:
                    str += "\n"
            return (str)

    def __repr__(self):
        """ ___repr__ """
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        """ __del__ """
        number_of_instances -= 1
        print("Bye rectangle...")
