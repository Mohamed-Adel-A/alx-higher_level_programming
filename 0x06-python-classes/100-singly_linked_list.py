#!/usr/bin/python3
""" define Singly linked list """

class Node:
    """ define node class """
    def __init__(self, data, next_node=None):
        """ init node calss """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ define a singly linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head = None:
            new_node.next_node = None
            self.__head = new_node
        else:
            node = self.__head
            while ((node.next_node is not None) and
                   (node.next_node.data < value)):
                node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node

    def __str__(self):
        nodes_data = list()
        node = self.__head
        while (node is not None):
            nodes_data.append(node.data)
            node = node.next_node
        return ('/n'.join(nodes_data))
