class Node:
    def __init__(self, info):
        self.info = info
        self.nextNode = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        n = int(input("Enter the nodes you want to create"))
        if n == 0 and n is None:
            print("INVALID ENTERY")
        for i in range(n):
            print("Enter {} value in list".format(i), end='')
            info = int(input())
            self.append(info)

    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.head.nextNode = self.head
            return
        p = self.head
        while p.nextNode != self.head:
            p = p.nextNode
        p.nextNode = temp
        temp.nextNode = self.head

    def prepend(self, data):
        temp = Node(data)
        p = self.head
        temp.nextNode = self.head
        if self.head is None:
            temp.nextNode = temp
            return
        while p.nextNode != self.head:
            p = p.nextNode
        p.nextNode = temp
        self.head = temp

    def add_node_after(self, key, data):
        temp = Node(data)
        p = self.head
        if self.head is None:
            print("List is empty")
            return
        while p.nextNode != self.head:
            if p.info == key:
                break
            p = p.nextNode

        if p is None:
            print(key, " not present in list")
        else:
            temp.nextNode = p.nextNode
            p.nextNode = temp

    def add_node_before(self, key, data):
        temp = Node(data)

        if self.head is None:
            print("List is Empty")
            return

        if self.head.info == key:
            p = self.head
            while p.nextNode != self.head:
                p = p.nextNode
            temp.nextNode = self.head
            p.nextNode = temp
            self.head = temp
            return

        p = self.head
        while p.nextNode != self.head:
            if p.nextNode.info == key:
                break
            p = p.nextNode

        if p.nextNode.info != key:
            print(key, "is not present in list")
        else:
            temp.nextNode = p.nextNode
            p.nextNode = temp

    def delete_node(self, key):
        p = self.head
        if self.head is None:
            print("List is Empty")
            return
        if self.head.info == key:
            while p.nextNode != self.head:
                p = p.nextNode
            p.nextNode = self.head.nextNode
            self.head = self.head.nextNode
            return
        while p.nextNode != self.head:
            prev = p
            p = p.nextNode
            if p.info == key:
                prev.nextNode = p.nextNode
                p = p.nextNode

    def remove_node(self, node):
        p = self.head
        if self.head == node:
            while p.nextNode != self.head:
                p = p.nextNode
            p.nextNode = self.head.nextNode
            self.head = self.head.nextNode
            return
        while p.nextNode != self.head:
            prev = p
            p = p.nextNode
            if p == node:
                prev.nextNode = p.nextNode
                p = p.nextNode

    def reverse_list(self):
        p = self.head
        if self.head is None:
            print("List is Empty")
            return
        prev = None
        while p.nextNode != self.head:
            next = p.nextNode
            p.nextNode = prev
            prev = p
            p = next
        p.nextNode = prev
        self.head.nextNode = p
        self.head = p

    def remove_duplicate(self):
        pass

    def pair_with_sum(self, sum_val):
        pass

    def josephus_problem(self, steps):
        p = self.head
        while self.count() > 1:
            count = 1
            while count != steps:
                p = p.nextNode
                count += 1
            print("REMOVE: " + str(p.info))
            self.remove_node(p)
            p = p.nextNode

    def split_list(self):
        size = self.count()
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size//2
        count = 0
        prev = None
        p = self.head
        # first list
        while p and count < mid:
            count += 1
            prev = p
            p = p.nextNode
        prev.nextNode = self.head

        # second list
        sl = CircularSinglyLinkedList()
        while p.nextNode != self.head:
            sl.append(p.info)
            p = p.nextNode
        sl.append(p.info)  # p is on last node we
                             # don't want to miss data so append here
        # print both list
        self.display()
        print('\n')
        sl.display()

    def display(self):
        p = self.head
        while p:
            print(p.info)
            p = p.nextNode
            if p == self.head:
                break

    def count(self):
        p = self.head
        n = 0
        while p:
            n += 1
            p = p.nextNode
            if p == self.head:
                break
        # print("Number of Node is List => {}".format(n))
        return n

list = CircularSinglyLinkedList()
list.create_list()

while True:
    print("=" * 40)
    print("1: Display List")
    print("2: Count Number Of List")
    print("3: Append Node")
    print("4: Prepend Node")
    print("5: Add Node After")
    print("6: Add Node Before")
    print("7: Delete Node")
    print("8: Reverse List")
    print("9: Remove Duplicate")
    print("10: Pair With Sum")
    print("12: Split List")
    print("13: Josephus problem")
    print("11: Quit")

    option = int(input("Enter Option"))

    if option == 1:
        list.display()
    elif option == 2:
        print("Total Node is {}".format(list.count()))
    elif option == 3:
        ele = int(input("Enter data"))
        list.append(ele)
    elif option == 4:
        ele = int(input("Enter data"))
        list.prepend(ele)
    elif option == 5:
        key = int(input("Enter the node after you want insert new node"))
        ele = int(input("Enter data"))
        list.add_node_after(key, ele)
    elif option == 6:
        key = int(input("Enter node before you want to insert new node"))
        ele = int(input("Enter data"))
        list.add_node_before(key, ele)
    elif option == 7:
        key = int(input("Enter the value to delete"))
        list.delete_node(key)
    elif option == 12:
        list.split_list()
    elif option == 13:
        steps = int(input("Enter the steps: "))
        list.josephus_problem(steps)
    elif option == 8:
        list.reverse_list()
    elif option == 11:
        print("Thanks for visiting.Over and Out")
        break
    else:
        print("Invalid option")