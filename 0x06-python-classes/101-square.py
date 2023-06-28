#!/usr/bin/python3
""" Defining a square class"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """ init a square instance """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size property """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    @property
    def position(self):
        """ position property """
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) or
                (len(value) != 2) or
                not (all(isinstance(element, int) for element in value)) or
                not (all(element >= 0 for element in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """ print square """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")

    def __str__(self):
        """ print a square """
        str = ""
        if self.size == 0:
            return("")
        else:
            for i in range(self.position[1]):
                str += "\n"
            for i in range(self.size):
                for k in range(self.position[0]):
                    str += " "
                for j in range(self.size):
                    str += "#"
                if i != self.size - 1:
                    str += "\n"
        return (str)
