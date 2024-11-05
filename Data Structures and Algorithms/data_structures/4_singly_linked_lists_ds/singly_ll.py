"""
Before creating the linked_list class we must define a node class.

Each instance of this class represents a single element (node) in the LL.

The class holds data for the node and a pointer to the next node.
"""


class Node(object):
    def __init__(
        self, data, n=None
    ):  # Constructor method called when a new instance is created
        self.data = data  # Assigns the data parameter to the instance variable self.data (holds the value for the node)
        self.next_node = (
            n  # Assigns the n parameter the instance variable next_node
        )

    def get_next(
        self,
    ):  # A getter method that returns the reference to the next node in the LL
        return (
            self.next_node
        )  # Returns the pointer to the next node when called

    def set_next(
        self, n
    ):  # Setter method that allows you to update the reference to the next node
        self.next_node = n

    def get_data(
        self,
    ):  # A getter method that returns the data stored in that particular node
        return self.data

    def self_data(
        self, d
    ):  # A method of updating the data stored in that node
        self.data = d


class LinkedList:
    def __init__(self):
        # Initialise the LinkedList with an empty head
        self.head = None
        # (Optional) Initialise with an empty tail - this can be allow a quicker method that prepend
        # self.tail = None

    def is_empty(self):
        # If the head is None then the list is empty and return True & VV
        return self.head is None

    def append(self, data):
        # Appends a new node with the given data at the end of the LinkedList
        new_node = Node(data)

        # Check if the list is empty, if it is add this as the head
        if self.head is None:
            self.head = new_node
        # Otherwise, traverse the list to the last node (until the pointer is None)
        else:
            current = self.head
            while (
                current.get_next() is not None
            ):  # The pointer being None is a common condition that we have reached the end
                current = current.get_next()
            # Set the last nodes pointer to the new node
            current.next_node = new_node

    def prepend(self, data):
        # Inserts a new node with the given data at the beginning of the LinkedList
        # -----------------------------------------------
        # Create new node with the data using Node class
        new_node = Node(data)

        # Point the new points pointer to the current head
        new_node.next_node = self.head

        # Update the head to the new node
        self.head = new_node

    def delete_first(self, data):
        # Deletes the **first/ all instances ?????** node containing the specified data
        current = self.head  # Starts at the head
        previous = None  # Keeps track of the previous node

        while (
            current is not None
        ):  # Iterate through the list from start to finish
            if current.get_data() == data:
                # If the data matches, delete this node
                if previous is None:
                    # If deleting the head node, set the next node to head
                    self.head = current.get_next()
                else:
                    # Otherwise, **bypass** the current node
                    previous.next_node = current.get_next()

            # Move to next node
            previous = current
            current = current.get_next()

    def insert(self, data, position):
        new_node = Node(data)

        # If inserting at the head (position 0)
        if position == 0:
            new_node.set_next(
                self.head
            )  # Set the pointer to the new node to the current head
            self.head = new_node  # Make the new point the head of the list
            return

        # Initialise current cell to head and index to 0
        current = self.head
        index = 0
        while current is not None and index < position - 1:
            current = current.get_next()
            index += 1

        # If the position is out of bounds of the linkedlist print feedback to user
        if current is None:
            print("Position out o bounds")
            return

        new_node.set_next(current.get_next())
        current.set_next(new_node)

    def display(self):
        # Prints the data in each node of the LinkedList
        # ----------------------------------------------
        # Initialise an empty list of nodes to append to
        nodes = []

        # Start from the head of the list
        current = self.head

        while current is not None:  # Iterate through entire list
            nodes.append(
                str(current.get_data())
            )  # Collect data from each node
            current = current.get_next()
        print("->".join(nodes))  # Print all nodes' data seperated by arrows.


# Example usage
# ---------------

# Create a new LinkedList
linked_list = LinkedList()

# Append five nodes with data values 1 through 5
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.delete(3)
linked_list.insert("three", 2)
# Display the linked list
linked_list.display()
