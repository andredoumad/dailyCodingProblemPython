# Andre Doumad
'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.head = None

    def solve(self, l1, l2):
        if l1 != None and l2 != None:
            if l1.val == l2.val:
                return l1
            else:
                return self.solve(l1.next, l2.next)

intersect = Node(8, Node(10, None))
l1 = Node(3, Node(7, intersect))
l2 = Node(99, Node(1, intersect))

solution = Solution()
result = solution.solve(l1, l2)
print('result is ', result, '\nwith a value of', result.val)

'''
OUTPUT:
result is  <__main__.Node object at 0x7f75d7c6df10> 
with a value of 8
'''