class Node(object):

    def __init__(self, info):
        self.info = info
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        self.start = None

    def create_list(self):
        n = int(input("Enter the number of nodes ypu want to create: "))
        if n == 0:
            return print("Invalid Entry")
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    def display(self):
        if self.start is None:
            print('List is Empty')
            return
        p = self.start
        while p is not None:
            print(p.info, " ", end='')
            p = p.next
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.next
        print("Number of node in the list =", n)

    def search(self, value):
        if self.start is None:
            print("list is empty")
            return
        position = 1
        p = self.start
        while p is not None:
            if p.info == value:
                print(value, " is at position", position)
                return
            position += 1
            p = p.next
        else:
            print(value, "Not found in list")
            return False

    def insert_at_start(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp

    def insert_after(self, data, value):
        p = self.start
        while p.next is not None:
            if p.info == value:
                break
            p = p.next
        if p is None:
            print(value, "is not present in List")
        else:
            temp = Node(data)
            temp.next = p.next
            p.next = temp

    def insert_before(self, data, value):
        if self.start is None:
            print("List is empty")
            return

        if value == self.start.info:
            temp = Node(data)
            temp.next = self.start
            self.start = temp
            return

        p = self.start
        while p.next is not None:
            if p.next.info == value:
                break
            p = p.next

        if p is None:
            print(value, "is not present in List")
        else:
            temp = Node(data)
            temp.next = p.next
            p.next = temp

    def insert_at_position(self, data, position):
        if position == 1:
            temp = Node(data)
            temp.next = self.start
            self.start = temp
            return

        p = self.start
        i = 1
        while i < position - 1 and p is not None:
            p = p.next
            i += 1

        if p is None:
            print("You can insert only upto position", i)
        else:
            temp = Node(data)
            temp.next = p.next
            p.next = temp

    def delete_node(self, value):
        if self.start is None:
            print('List is Empty')
            return

        if self.start.info == value:
            self.start = self.start.next
            return

        p = self.start
        while p.next is not None:
            if p.next.info == value:
                break
            p = p.next

        if p.next is None:
            print("Element ", value, "not in list")
        else:
            p.next = p.next.next

    def delete_first_node(self):
        if self.start is None:
            print("List is empty")
            return
        self.start = self.start.next

    def delete_last_node(self):
        if self.start is None:
            print("List is Empty")
            return

        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next.next is not None:
            p = p.next
        p.next = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            nextlink = p.next
            p.next = prev
            prev = p
            p = nextlink
        self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.next:
            p = self.start
            while p.next != end:
                q = p.next
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.next
            end = p

    def bubble_sort_exlink(self):
        end = None
        while end != self.start.next:
            r = p = self.start
            while p.next != end:
                q = p.next
                if p.info > q.info:
                    p.next = q.next
                    q.next = p
                    if p != self.start:
                        r.next = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.next
            end = p

    def has_cycle(self):
        pass

    def merge_sort(self):
        pass

    def insert_cycle(self, data):
        pass


List = SinglyLinkedList()
List.create_list()

while True:
    print("1. Display List")
    print("2. Count the number of Nodes in List")
    print("3. Search for an Element in List")
    print("4. Insert in Empty list/ Insert at the start position of the List")
    print("5. Insert the Node at the end of the List")
    print("6. Insert Node after a specified Node")
    print("7. Insert Node before a specified Node")
    print("8. Insert Node at a given position")
    print("9. Delete first Node")
    print("10. Delete last Node")
    print("11. Delete any Node")
    print("12. Reverse List")
    print("13. Bubble sort by exchanging Links")
    print("14. Bubble sort by exchanging Links")
    print("15. MergeSort")
    print("16. Insert Cycle")
    print("17. Delete Cycle")
    print("18. Remove Cycle")
    print("19. Quit")

    option = int(input("Enter the your choice: "))

    if option == 1:
        List.display()
    elif option == 2:
        List.count_nodes()
    elif option == 3:
        ele = int(input("Enter the Element which you want to search"))
        List.search(ele)
    elif option == 4:
        ele = int(input("Enter the Element to insert at start position of List"))
        List.insert_at_start(ele)
    elif option == 5:
        ele = int(input("Enter the Element to insert at end position of List "))
        List.insert_at_end(ele)
    elif option == 6:
        ele = int(input("Enter the Element to be insert"))
        place = int(input("Enter the Element after which to insert"))
        List.insert_after(ele, place)
    elif option == 7:
        ele = int(input("Enter the Element to be insert"))
        place = int(input("Enter the Element before which to insert"))
        List.insert_before(ele, place)
    elif option == 8:
        ele = int(input("Enter the Element to be insert"))
        place = int(input("Enter the position at which to insert"))
        List.insert_at_position(ele, place)
    elif option == 9:
        List.delete_first_node()
    elif option == 10:
        List.delete_last_node()
    elif option == 11:
        ele = int(input("Enter the Element to be deleted"))
        List.delete_node(ele)
    elif option == 12:
        List.reverse_list()
    elif option == 13:
        List.bubble_sort_exdata()
    elif option == 14:
        List.bubble_sort_exlink()
    elif option == 15:
        pass
    elif option == 16:
        pass
    elif option == 17:
        pass
    elif option == 18:
        pass
    elif option == 19:
        break
    else:
        print("Wrong option")
    print()

