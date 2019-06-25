class Node:

    def __init__(self, info):
        self.info = info
        self.nextNode = None
        self.prevNode = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None

    def create_list(self):
        n = int(input("Enter number to create List"))
        if n == 0 and n is None:
            print("Invalid Entry")
            return

        for i in range(n):
            print("Enter data for {} Node".format(i), end='')
            info = int(input())
            self.append(info)

    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.head.prevNode = self.head
            self.head.nextNode = self.head
            return

        p = self.head
        while p.nextNode != self.head:
            p = p.nextNode
        temp.prevNode = p
        temp.nextNode = self.head
        p.nextNode = temp
        self.head.prevNode = temp

    def prepend(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.head.prevNode = self.head
            self.head.nextNode = self.head
            return
        p = self.head
        while p.nextNode != self.head:
            p = p.nextNode
        temp.nextNode = self.head
        temp.prevNode = p
        self.head.prevNode = temp
        p.nextNode = temp
        self.head = temp

    def add_node_after(self, key, data):
        temp = Node(data)
        p = self.head
        if self.head is None:
            print("Empty List")
            return

        if self.head.prevNode.info == key:
            temp.nextNode = self.head
            temp.prevNode = self.head.prevNode
            self.head.prevNode.nextNode = temp
            self.head.prevNode = temp
            return

        while p.nextNode != self.head:
            if p.info == key:
                break
            p = p.nextNode

        if p.info != key:
            print(key, "is not present in List")
            return
        else:
            temp.nextNode = p.nextNode
            temp.prevNode = p
            p.nextNode = temp
            p.nextNode.prevNode = temp

    def add_node_before(self, key, data):
        temp = Node(data)
        p = self.head
        if self.head is None:
            print("Empty List")
            return

        if self.head.info == key:
            while p.nextNode != self.head:
                p = p.nextNode

            temp.nextNode = self.head
            temp.prevNode = p
            self.head.prevNode = temp
            p.nextNode = temp
            self.head = temp
            return

        while p.nextNode != self.head:
            if p.nextNode.info == key:
                break
            p = p.nextNode

        if p.nextNode.info != key:
            print(key, "is not present in list")
            return
        else:
            temp.nextNode = p.nextNode
            temp.prevNode = p
            p.nextNode.prevNode = temp
            p.nextNode = temp

    def insert_at_location(self, loc, data):
        temp = Node(data)
        p = self.head
        count = self.count()

        if self.head is None:
            print("Empty List")
            return

        if loc == 1:
            temp.nextNode = self.head
            temp.prevNode = self.head.prevNode
            self.head.prevNode.nextNode = temp
            self.head.prevNode = temp
            self.head = temp
            return

        i = 1

        while i < loc-1 and p is not None:
            p = p.nextNode
            i += 1

        if loc > count:
            print("Not valid location")
            return
        else:
            temp.nextNode = p.nextNode
            temp.prevNode = p
            p.nextNode.prevNode = temp
            p.nextNode = temp

    def delete_node(self, value):
        p = self.head
        prev = None

        if self.head is None:
            print("Empty List")
            return

        while p.info != value:
            if p.nextNode == self.head:
                print(value, " is not present in List")
                return
            prev = p
            p = p.nextNode

        if p.nextNode == self.head and prev is None:
            print("{} is deleted".format(p.info))
            self.head = None
            return

        elif p == self.head:
            print("{} is deleted".format(p.info))
            prev = p.prevNode
            self.head = self.head.nextNode
            prev.nextNode = self.head
            self.head.prevNode = prev
            return

        elif p.nextNode == self.head:
            print("{} is deleted".format(p.info))
            prev.nextNode = self.head
            self.head.prevNode = prev
            return

        else:
            print("{} is deleted".format(p.info))
            prev.nextNode = p.nextNode
            p.nextNode.prevNode = prev
            p = p.nextNode
            return

    def reverse(self):
        pass


    def display(self):
        if self.head is None:
            print("Empty List")
            return
        p = self.head
        while p:
            print(p.info)
            p = p.nextNode
            if p == self.head:
                break

    def count(self):
        if self.head is None:
            print("Empty List")
            return
        n = 0
        p = self.head
        while p:
            n += 1
            p = p.nextNode
            if p == self.head:
                break
        return n

list = CircularDoublyLinkedList()
list.create_list()

while True:
    print("=" * 40)
    print("1: Display")
    print("2: Append")
    print("3: Prepend")
    print("4: Count Nodes")
    print("5: Insert Node After")
    print("6: Insert Node Before")
    print("7: Insert Node at Position")
    print("8: Remove Node")
    print("9: QUIT")

    option = int(input("Enter your option"))
    if option == 1:
        list.display()
    elif option == 2:
        ele = int(input("Enter data"))
        list.append(ele)
    elif option == 4:
        print("Number of Nodes {}".format(list.count()))
    elif option == 3:
        ele = int(input("Enter data"))
        list.prepend(ele)
    elif option == 5:
        key = int(input("Enter key after you insert Node"))
        data = int(input("Enter data"))
        list.add_node_after(key, data)
    elif option == 6:
        key = int(input("Enter key before you insert Node"))
        data = int(input("Enter data"))
        list.add_node_before(key, data)
    elif option == 7:
        loc = int(input("Enter position"))
        data = int(input("Enter data"))
        list.insert_at_location(loc, data)
    elif option == 8:
        ele = int(input("Enter the key you want to delete"))
        list.delete_node(ele)
    elif option == 9:
        print("Thanks for visiting.Over and Out")
        break
    else:
        print("Invalid option")


