'''
Daily Coding Problem: Problem #8 [Easy]
This problem was asked by Google.

A unival tree (which stands for "universal value") is a 
tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
We will be sending the solution tomorrow, along with tomorrow's question. 
'''
import sys
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node0 = Node(0)
node1 = Node(1)
node0.left = node1
node2 = Node(0)
node0.right = node2
node3 = Node(1)
node2.left = node3
node4 = Node(0)
node2.right = node4
node3.left = Node(1)
node3.right = Node(1)

def printTree(node, indent, last):
    if node:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write('R----')
            indent += '    '
        else:
            sys.stdout.write('L----')
            indent += '|   '
        print(str(node.data))
        printTree(node.left, indent, False)
        printTree(node.right, indent, True)

printTree(node0, "", True)

def findUnivals(node):
    univals = 0
    def solve(node):
        if node:
            if node.left ==None and node.right ==None:
                univals += 1
            elif node.left != None and node.right != None:
                if node.left.data == node.right.data:
                    univals +=1
            if node.left:
                solve(node.left)
            if node.right:
                solve(node.right)
    return univals

print(findUnivals(node0))
