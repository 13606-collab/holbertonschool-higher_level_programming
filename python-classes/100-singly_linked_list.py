#!/usr/bin/python3
"""
This module defines a Singly Linked List and its Nodes.
It allows for sorted insertion of integers into a linked list structure
to maintain an increasing order.
"""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        __data (int): The integer value stored in the node.
        __next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data value for the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data with type validation.

        Args:
            value (int): The integer value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next_node.

        Returns:
            Node: The next node in the sequence.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node with validation.

        Args:
            value (Node): The Node object or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        __head (Node): The first node of the list.
    """

    def __init__(self):
        """Initializes an empty Singly Linked List."""
        self.__head = None

    def __str__(self):
        """
        Defines the printable representation of the list.
        Each node's data is printed on a new line.

        Returns:
            str: The formatted string of all node values.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Find the correct position in the middle or end
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node#!/usr/bin/python3
"""
This module defines a Singly Linked List and its Nodes.
It allows for sorted insertion of integers into a linked list structure
to maintain an increasing order.
"""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        __data (int): The integer value stored in the node.
        __next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data value for the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data with type validation.

        Args:
            value (int): The integer value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next_node.

        Returns:
            Node: The next node in the sequence.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node with validation.

        Args:
            value (Node): The Node object or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        __head (Node): The first node of the list.
    """

    def __init__(self):
        """Initializes an empty Singly Linked List."""
        self.__head = None

    def __str__(self):
        """
        Defines the printable representation of the list.
        Each node's data is printed on a new line.

        Returns:
            str: The formatted string of all node values.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Find the correct position in the middle or end
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
