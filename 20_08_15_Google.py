# Andre Doumad
'''
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution():
    def solve(self, l, target):
        print('solve')
        prev = l
        curr = l
        while curr != None:
            if curr.val == target:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        return l

l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
temp = l
print('before: ')
while temp != None:
    print(temp.val)
    temp = temp.next
solution = Solution()
result = solution.solve(l, 3)
temp = result
print('after: ')
while temp != None:
    print(temp.val)
    temp = temp.next
'''
output:
before: 
1
2
3
4
5
solve
after: 
1
2
4
5
'''