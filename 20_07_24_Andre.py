'''
Andre Doumad 

Daily Coding Problem: Problem #4 [Hard]

This is your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

We will be sending the solution tomorrow, along with tomorrow's question.
'''

import unittest

class minHeap(object):
    #heap
    def __init__(self):
        self.heap=[]

    #get parent, left, right
    def getParent(self,i):
        return int((i-1)/2)
    def getLeft(self,i):
        return 2*i+1
    def getRight(self,i):
        return 2*i+2

    #has parent, left, right
    def hasParent(self,i):
        return self.getParent(i)>=0
    def hasLeft(self,i):
        return self.getLeft(i)<len(self.heap)
    def hasRight(self,i):
        return self.getRight(i)<len(self.heap)
    #heapify down
    def heapifyDown(self,i):
        while self.hasLeft(i):
            min_child = self.minChild(i)
            if min_child == -1:
                break
            if self.heap[i] > self.heap[min_child]:
                self.swap(min_child, i)
                i = min_child
            else:
                break

    #swap
    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    #heapify up
    def heapifyUp(self,i):
        while self.hasParent(i) and self.heap[self.getParent(i)] > self.heap[i]:
            self.swap(i, self.getParent(i))
            i = self.getParent(i)


    #get min child
    def minChild(self,i):
        if self.hasLeft(i):
            left_index = self.getLeft(i)
            if self.hasRight(i):
                right_index = self.getRight(i)
                if self.heap[right_index] > self.heap[left_index]:
                    return left_index
                else:
                    return right_index
            else:
                return -1
        else:
            return -1

    #popMin
    def popMin(self):
        if len(self.heap) == 0:
            return None
        if self.heap[0] < self.heap[len(self.heap)-1]:
            self.swap(0, len(self.heap)-1)
        val = self.heap.pop()
        self.heapifyDown(0)
        return val

    #insert
    def insert(self, key):
        if len(self.heap) == 0:
            self.heap.append(key)
            return
        self.heap.append(key)
        self.heapifyUp(len(self.heap)-1)


# solution
class Solution_A(object):
    def solve(self, a):
        print(a)
        minheap = minHeap()
        for element in a:
            minheap.insert(element)
        print(minheap.heap)
        # for i in range(0,len(minheap.heap)):
        #     print(minheap.heap)
        #     print('debug: ' + str(minheap.popMin()))
        # exit()
        last_val = minheap.popMin()
        # print('last_val: ' + str(last_val))
        current_val = minheap.popMin()
        # print('current_val: ' + str(current_val))
        missing_val = 0
        found = False
        working = True
        while working:
            if current_val == None:
                # print('current_val = None')
                working = False
            if last_val +1 > 0 and last_val + 1 != current_val:
                print('found missing val')
                missing_val = last_val+1
                found = True
                working = False
            else:
                last_val = current_val
                # print('last_val: ' + str(last_val))
                current_val = minheap.popMin()
                # print('current_val: ' + str(current_val))
        if found:
            print('missing_val: ' + str(missing_val))
        else:
            print('there is no spoon')


# unittest
class unitTest(unittest.TestCase):
    def test_A(self):
        solution = Solution_A()
        solution.solve([1,2,0])
        solution.solve([3,4,-1,1])
        solution.solve([7,5,3,4,9,0,-1,1,2,6])


if __name__ == '__main__':
    unittest.main()