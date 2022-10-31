import re


class Node():
    def __init__(self, DataItems=None):
        self.items = DataItems
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print("{} ".format(temp.items), end="")
            if temp.next is not None:
                print("<-", end=" ")
            temp = temp.next

    def append(self, item):
        temp_node = Node(item)
        if self.head is None:
            self.head = temp_node
            return
        last_node = self.head
        while (last_node.next):
                last_node = last_node.next
        last_node.next = temp_node

    def moveToEnd(self, item):
        first_node = self.head
        last_node = self.head
        while (last_node.next != None) :
                last_node = last_node.next
        if first_node.items != item:
            
            last_node.next = Node(first_node.items)
            self.head = self.head.next
                

list_loco = LinkedList()

list_loco.append("A")
list_loco.append("B")
list_loco.append("C")
list_loco.moveToEnd("A")


list_loco.printList()