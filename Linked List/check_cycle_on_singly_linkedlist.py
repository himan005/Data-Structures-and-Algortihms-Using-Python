from nose.tools import assert_equal


def check_cycle(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True
    return False

class Node(object):

    def __init__(self, info):
        self.info = info
        self.nextnode = None

"""
TEST SOLUTION
"""

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a

class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("All test cases passed")

t = TestCycleCheck()

t.test(check_cycle)