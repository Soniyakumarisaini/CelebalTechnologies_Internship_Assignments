
# Assignment2: Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return

        if n <= 0:
            print("Invalid index.")
            return

        if n == 1:
            deleted = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position {n}: {deleted}")
            return

        current = self.head
        for _ in range(n - 2):
            if current.next is None:
                print("Index out of range.")
                return
            current = current.next

        if current.next is None:
            print("Index out of range.")
            return

        deleted = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n}: {deleted}")

#Sample Test Code

if __name__ == "__main__":
    ll = LinkedList()

    # Add sample nodes
    ll.add_node(2)
    ll.add_node(4)
    ll.add_node(6)
    ll.add_node(8)

    print("Original Linked List:")
    ll.print_list()

    ll.delete_nth_node(2)

    print("Linked List after deleting 2nd node:")
    ll.print_list()

    ll.delete_nth_node(10)  # out of range

    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    ll.delete_nth_node(1)  # list is empty
