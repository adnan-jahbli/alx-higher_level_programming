#!/usr/bin/python3

"""Defining a classes for a singly linked list."""


class Node:
    """Representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializing a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Representing a singly linked list."""

    def __init__(self):
        """Initializing a new singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node to the singly linked list.

        The node is inserted to the list at the correct
        ordered position.

        Args:
            value (Node): The new Node to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    value >= current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        if self.head is None:
            return ""
        current = self.head
        result = str(current.data)
        while current.next_node is not None:
            current = current.next_node
            result += "\n" + str(current.data)
        return result
