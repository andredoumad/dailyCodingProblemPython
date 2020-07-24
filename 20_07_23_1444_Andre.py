# Andre Doumad
# Daily Coding Problem: Problem #3 [Medium]
# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

import sys, pickle

# Node 
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(node, indent, last):
    if node:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write('R----')
            indent += '    '
        else:
            sys.stdout.write('L----')
            indent += '|   '
        print(str(node.val))
        printTree(node.left, indent, False)
        printTree(node.right, indent, True)

def serialize(node):
    print('serialize')
    printTree(node, "", True)
    with open('20_07_23_1444_Andre_out.txt', 'wb') as rick:
       pickle.dump(node, rick)

def deserialize(node):
    with open('20_07_23_1444_Andre_out.txt', 'rb') as rick:
        pickleNode = pickle.load(rick)
        print(str(pickleNode))
        printTree(pickleNode, "", True)
        return pickleNode

# test
node = Node('root', Node('left', Node('left.left')), Node('right'))
serialize(node)
assert deserialize(serialize(node)).left.left.val == 'left.left'
