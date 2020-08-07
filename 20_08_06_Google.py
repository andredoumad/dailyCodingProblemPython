# Andre Doumad
'''
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

# break string into list of filepaths
    # tabs denote depth
    # periods denote files
    # names without periods denote folders

# load filepaths into N-array tree
    # each node has list of children
    # children can be files or folders

# visit all nodes in tree, find longest absolute file path, or return 0 if no files were present.

import unittest, sys

class Node(object):
    def __init__(self, parent, directory, value, depth):
        self.parent = parent
        self.directory = directory
        self.value = value
        self.children = []
        self.depth = depth


class Solution(object):
    def __init__(self):
        self.root = None
        self.filepaths = []

    def insertNode(self, parent, directory, depth, value):
        return self.doInsertNode(self.root, parent=parent, directory=directory, depth=depth,value=value)

    def doInsertNode(self, node, parent, directory, depth, value):
        if self.root == None:
            self.root = Node(parent=None, directory=directory, value=value, depth=depth)
            return self.root
        if depth > node.depth:
            if len(node.children) > 0:
                print('looking through children')
                for child in node.children:
                    return self.doInsertNode(child, parent=parent, directory=directory, depth=depth,value=value)
            else:
                print('inserting child')       
                newNode = Node(parent=node, directory=directory, value=value, depth=depth)   
                node.children.append(newNode)

                print('newNode = ', newNode)
                print('newNode parent value = ', newNode.parent.value)
                return newNode.parent.value
        if depth == node.depth:
            print('inserting child')       
            newNode = Node(parent=node, directory=directory, value=value, depth=depth)   
            node.children.append(newNode)

            print('newNode = ', newNode)
            print('newNode parent value = ', newNode.parent.value)
            return newNode.parent.value



    def decodePaths(self, n):
        paths = []
        previousStartIndex = 0
        i = 0
        decoding = True
        strings = []
        tempString = ''
        extension = False
        n = n.split('\n')
        print(n)
        parent = None
        for string in n:
            depth = string.split('\t')
            depth = len(depth)-1
            print(string + ' depth ' + str(depth))
            directory = False
            if string.find('.') != -1:
                directory = False
            else:
                directory = True
            print('parent is ' + str(parent))
            parent = self.insertNode(parent=parent, directory=directory, value=string, depth=depth)
            if parent == None:
                print(' parent is none!')
                exit()
            # parent = string

        self.printTree()


    def printTree(self):
        self.doPrintTree(self.root, "", True)
    
    def doPrintTree(self, node, indent, last):
        if node:
            sys.stdout.write(indent)
            if last:
                print('------')
                indent += "     "
            else:
                print('------')
                indent += "     "
            if node.parent != None:
                print('n: ', node.value, ' p: ', node.parent.value)
            else:
                print('n: ', node.value, ' p: ', 'None')
            for child in node.children:
                self.doPrintTree(child, indent, False)
            # print(node.value)


    def inOrderTraversal(self, node):
        if node:
            print(node.value)
            for child in node.children:
                self.inOrderTraversal(child)

    def makefilepaths(self, node):
        self.doFilepaths(node, "")


    def getParent(self, node):
        if node.parent != None:
            print('node: ', node.value, ' parent is ', node.parent.value)
        return node.parent

    def doFilepaths(self, node, filepath):
        if node:
            # print('node: ' + node.value)
            self.getParent(node)
            if node.directory == False:
                parents = []
                myparent = node
                while self.getParent(myparent) != None:
                    parents.append(myparent.parent.value)
                    myparent = self.getParent(myparent)
                print('PARENTS: ' + str(parents)) 
                # exit()
                self.filepaths.append(str(filepath) + str(node.value))
            else:
                filepath += str(node.value)
                print('filepath ' + filepath)

            for child in node.children:
                self.doFilepaths(child, filepath)


    def solve(self, n):
        self.decodePaths(n)
        self.inOrderTraversal(self.root)
        self.makefilepaths(self.root)
        print('self.filepaths ', self.filepaths)
        longestPath = ''
        for path in self.filepaths:
            print(path)
            if len(path) > len(longestPath):
                longestPath = path
        
        
        return longestPath


class unitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print('''dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext''')
        result = solution.solve('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
        print('RESULT: ' + str(result))

if __name__ == '__main__':
    unittest.main()