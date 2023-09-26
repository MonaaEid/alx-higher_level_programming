#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """
    A class used to represent a node of a singly linked list.

    Attributes
    ----------
    data : int
        an integer representing the data stored in the node
    next_node : Node
        a reference to the next node in the linked list

    Methods
    -------
    __init__(self, data, next_node=None):
        Initializes a new instance of the Node class.
        Parameters:
            data (int): an integer representing the data stored in the node
            next_node (Node): a reference to the next node
            in the linked list (default None)
        Raises:
            TypeError: if data is not an integer or if next_node is not None
            or a Node object

    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns the value of the private instance attribute `data`.

        Returns:
            int: an integer representing the data stored in the node

        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the value of the private instance attribute `data`.

        Parameters:
            value (int): an integer representing the data stored in the node
        Raises:
            TypeError: if value is not an integer

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Returns the value of the private instance attribute `next_node`.

        Returns:
            Node: a reference to the next node in the linked list

        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of the private instance attribute `next_node`.

        Parameters:
            value (Node): a reference to the next node
            in the linked list (default None)
        Raises:
            TypeError: if value is not None or a Node object

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class used to represent a singly linked list.

    Attributes
    ----------
    head : Node
        a reference to the first node in the linked list

    Methods
    -------
    __init__(self):
        Initializes a new instance of the SinglyLinkedList class.
    sorted_insert(self, value):
        Inserts a new Node into the correct sorted
        position in the list (increasing order).

         Parameters:
            value (int): an integer representing
            the data stored in the new node.
         Raises:
            TypeError: if value is not an integer.

     __str__(self):
         Returns a string representation of all
         nodes in this singly linked list
         Returns:
             str: A string representation of all
             nodes in this singly linked list
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node.next_node is not None and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
