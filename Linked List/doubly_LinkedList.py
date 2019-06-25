class Node(object):

    def __init__(self, info):
        self.info = info
        self.nextNode = None
        self.prevNode = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, data):
        temp = Node(data)
        if self.head is None:       # if head is None that means List is empty
            temp.prevNode = None    # we create node as first node
            self.head = temp
            return
        p = self.head
        while p.nextNode:           # if head is Not empty then we move pointer p till the node next is None
            p = p.nextNode          # moving p pointer to next of node and resign back to pointer p
        p.nextNode = temp           # Now p is on last node of List and assign new node to it's next
        temp.prevNode = p           # assign p pointer to prev of new node that is temp
        temp.nextNode = None        # assign None to next of new node

    def prepend(self, data):
        temp = Node(data)
        if self.head is None:      # if List is Empty
            temp.prevNode = None   # create new node in list
            self.head = temp       # assign new node to head pointer
            return
        self.head.prevNode = temp  # connect to first node of list to new node
        temp.nextNode = self.head  # connect new node to first node of list
        self.head = temp           # move head pointer to new node
        temp.prevNode = None       # assign none to prev of new node

    def add_node_after(self, key, data):
        p = self.head
        while p:
            if p.nextNode is None and p.info == key:  # case  => when there is only one node in list
                self.append(data)
                return
            if p.info == key:   # when key found in lit
                temp = Node(data)   # create new node
                nex = p.nextNode    # create pointer next to key node
                p.nextNode = temp
                temp.nextNode = nex
                temp.prevNode = p
                nex.prevNode = temp
            p = p.nextNode
            if p is None:   # when no key  found in list
                print(key, " Not found in List")
                return


    def add_node_before(self, key, data):
        p = self.head
        while p:
            if p.prevNode is None and p.info == key:   # when only one node in list
                self.prepend(data)
                return
            if p is None:   # when not key in List
                print(key, "Not found in List")
                return
            if p.info == key:
                temp = Node(data)
                prev = p.prevNode
                prev.nextNode = temp
                p.prevNode = temp
                temp.nextNode = p
                temp.prevNode = prev
            p = p.nextNode

    def delete_node(self, key):
        p = self.head
        while p:
            # case 1 when one node in list and nextNode is None
            if p.info == key and p == self.head:
                if not p.nextNode:
                    p = None
                    self.head = None
                    return
                # case 2 when nextNode of 1st node is not None
                else:
                    nex = p.nextNode
                    p.nextNode = None
                    nex.prevNode = None
                    p = None
                    self.head = nex
                    return
            if p.info == key:
                # case 3 when is between 1st and last node of list
                if p.nextNode:
                    nxt = p.nextNode
                    prev = p.prevNode
                    prev.nextNode = nxt
                    nxt.prevNode = prev
                    p.nextNode = None
                    p.prevNode = None
                    p = None
                    return
                else:
                    # case 4 when last node remove from list
                    prev = p.prevNode
                    prev.nextNode = None
                    p.prevNode = None
                    p = None
                    return
            p = p.nextNode

    def reverse_list(self):
        temp = None     # create a pointer
        p = self.head   # create a pointer assign head
        # Swap next and prev for all nodes of
        # doubly linked list
        while p:
            temp = p.prevNode
            p.prevNode = p.nextNode
            p.nextNode = temp
            p = p.prevNode
        if temp:
            self.head = temp.prevNode

    def remove_duplicate(self):
        p = self.head
        seen = dict()
        while p:
            if p.info not in seen:
                seen[p.info] = 1
                p = p.nextNode
            else:
                nxt = p.nextNode
                self.delete_dup(p)
                p = nxt

    def delete_dup(self, node):
        p = self.head
        while p:
            # case 1 when one node in list and nextNode is None
            if p == node and p == self.head:
                if not p.nextNode:
                    p = None
                    self.head = None
                    return
                # case 2 when nextNode of 1st node is not None
                else:
                    nex = p.nextNode
                    p.nextNode = None
                    nex.prevNode = None
                    p = None
                    self.head = nex
                    return
            if p == node:
                # case 3 when is between 1st and last node of list
                if p.nextNode:
                    nxt = p.nextNode
                    prev = p.prevNode
                    prev.nextNode = nxt
                    nxt.prevNode = prev
                    p.nextNode = None
                    p.prevNode = None
                    p = None
                    return
                else:
                    # case 4 when last node remove from list
                    prev = p.prevNode
                    prev.nextNode = None
                    p.prevNode = None
                    p = None
                    return
            p = p.nextNode

    def create_list(self):
        n = int(input("Enter number of Nodes you want to create: "))
        if n is None and n == 0:
            return "Invalid Entry"
        for i in range(n):
            print("Enter {} element in List: ".format(i), end='')
            info = int(input())
            self.append(info)

    def count_nodes(self):
        p = self.head
        n = 0
        while p is not None:
            n += 1
            p = p.nextNode
        print("Number of Nodes in List: {}".format(n))

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        p = self.head
        while p is not None:
            print(p.info, " ", end='')
            p = p.nextNode
            print()

    def pair_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.nextNode
            while q:
                if p.info + q.info == sum_val:
                    pairs.append("(" + str(p.info) + ", " + str(q.info) + ")")
                q = q.nextNode
            p = p.nextNode
        return pairs

    # function to do merge Sort
    def merge_sort(self, temphead):
        if temphead is None:
            return temphead
        if temphead.nextNode is None:
            return temphead
        list2 = self.split_list(temphead)

        temphead = self.merge_sort(temphead)
        list2 = self.merge_sort(list2)
        return self.merge_list(temphead, list2)

    # function to merge list
    def merge_list(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.info < list2.info:
            list1.nextNode = self.merge_list(list1.nextNode, list2)
            list1.nextNode.prevNode = list1.nextNode
            list1.prevNode = None
            return list1
        else:
            list2.nextNode = self.merge_list(list1, list2.nextNode)
            list2.nextNode.prevNode = list2
            list2.prevNode = None
            return list2

    # function to split list
    def split_list(self, temphead):
        slow = temphead
        fast = temphead
        while True:
            if fast.nextNode is None:
                break
            if fast.nextNode.nextNode is None:
                break
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
        temp = slow.nextNode
        slow.nextNode = None
        return temphead

List = DoublyLinkedList()
List.create_list()

while True:
    print("=" * 40)
    print("OPTION TO PERFORM OVER LINKED LIST")
    print("1: Display_List")
    print("2: Count Number Of Nodes")
    print("3: Append Node")
    print("4: Prepend Node")
    print("6: Add Node After")
    print("7: Add Node Before")
    print("8: Delete Node")
    print("9: Reverse List")
    print("10: Remove Duplicate")
    print("11: Pair With Sum")
    print("12: Merge Sort")
    print("5: Quit")

    option = int(input("Choose an option "))

    if option == 1:
        List.display()
    elif option == 2:
        List.count_nodes()
    elif option == 3:
        ele = int(input("Enter Element to insert at end of Linked List"))
        List.append(ele)
    elif option == 5:
        print("Thanks For Visiting. Over And Out")
        break
    elif option == 4:
        ele = int(input("Enter Element to Prepend To Linked List"))
        List.prepend(ele)
    elif option == 6:
        ele = int(input("Enter Element to add"))
        key = int(input("Enter key add element after"))
        List.add_node_after(key,  ele)
    elif option == 7:
        ele = int(input("Enter Element to add"))
        key = int(input("Enter key add element before"))
        List.add_node_before(key,  ele)
    elif option == 8:
        key = int(input("Enter key to delete node"))
        List.delete_node(key)
    elif option == 9:
        List.reverse_list()
    elif option == 10:
        List.remove_duplicate()
    elif option == 11:
        sum_val = int(input("enter sum value"))
        print(List.pair_with_sum(sum_val))
    elif option == 12:
        List.merge_sort(List.head)
        List.Display()
    else:
        print("Invalid option")
