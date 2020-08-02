# Andre Doumad
'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

import unittest,sys
  
class MinHeap: 
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.heap = [0]*(self.maxsize + 1) 
        # biggest possible heap for system by setting first element to lowest possible
        # system value
        self.heap[0] = -1 * sys.maxsize
        print('self.heap[0] : ' + str(self.heap[0]))
        self.front = 1
    
    # get parent, left or right
    def parent(self, index): 
        return index//2
    def leftChild(self, index): 
        return 2 * index 
    def rightChild(self, index): 
        return (2 * index) + 1

    def isLeaf(self, index): 
        if index >= (self.size//2) and index <= self.size: 
            return True
        return False
    
    def swap(self, a, b): 
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a] 
  
    def minHeapify(self, index): 
        if not self.isLeaf(index): 
            if (self.heap[index] > self.heap[self.leftChild(index)] or 
               self.heap[index] > self.heap[self.rightChild(index)]): 
                # swap with left child
                if self.heap[self.leftChild(index)] < self.heap[self.rightChild(index)]: 
                    self.swap(index, self.leftChild(index)) 
                    self.minHeapify(self.leftChild(index)) 
                # Swap with right child
                else: 
                    self.swap(index, self.rightChild(index)) 
                    self.minHeapify(self.rightChild(index)) 

    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.heap[self.size] = element   
        current = self.size 
        while self.heap[current] < self.heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 

    def minHeap(self): 
        for index in range(self.size//2, 0, -1):
            print('minHeapify index: ' + str(index))
            self.minHeapify(index) 
  
    def remove(self): 
        popped = self.heap[self.front] 
        self.heap[self.front] = self.heap[self.size] 
        self.size-= 1
        self.minHeapify(self.front) 
        return popped 

    def printHeap(self):
        for i in range(1, (self.size//2)+1): 
            print(" parent: "+ str(self.heap[i])+" left: "+ str(self.heap[2 * i])+" right: " + str(self.heap[2 * i + 1])) 

class Solution(object):
    def solve(self, inputArray, k):
        mHeap= MinHeap(len(inputArray)+ 2)
        for element in inputArray:
            mHeap.insert(element)
        mHeap.minHeap()
        numbers = []
        popping = True
        mHeap.printHeap()
        # exit()
        for i in range(0, len(inputArray)):
            number = mHeap.remove()
            if number > k:
                print('mHeap is returning numbers larger than k')
                print('mheap returned ' + str(number))
                break
            else:
                print('mHeap min is: ' + str(number))
                numbers.append(number)
        for i in range(0, len(numbers)):
            a = numbers[i]
            for j in range(0, len(numbers)):
                if j != i:
                    b = numbers[j]
                    print('adding ' + str(a) + ' + ' + str(b))
                    result = a+b
                    print('testing result: ' + str(result))
                    if b + a == k:
                        return True
        return False

class unitTest(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        result = solution.solve([33, 57, 200, 99, 11, 5, 1, 100, 55, 333, 666, 420, 10, 15, 3, 7], 257)

        print('RESULT IS : ' + str(result))
        self.assertTrue(solution.solve, "return true since 10 + 7 is 17.")

        result = solution.solve([10, 15, 3, 7], 17)
        print('RESULT IS : ' + str(result))
        self.assertTrue(solution.solve, "return true since 10 + 7 is 17.")

if __name__ == '__main__':
    unittest.main()

'''
OUTPUT:

self.heap[0] : -9223372036854775807
minHeapify index: 8
minHeapify index: 7
minHeapify index: 6
minHeapify index: 5
minHeapify index: 4
minHeapify index: 3
minHeapify index: 2
minHeapify index: 1
 parent: 1 left: 7 right: 3
 parent: 7 left: 33 right: 57
 parent: 3 left: 10 right: 5
 parent: 33 left: 55 right: 99
 parent: 57 left: 333 right: 666
 parent: 10 left: 420 right: 200
 parent: 5 left: 15 right: 11
 parent: 55 left: 100 right: 0
mHeap min is: 1
mHeap min is: 3
mHeap min is: 5
mHeap min is: 7
mHeap min is: 10
mHeap min is: 11
mHeap min is: 15
mHeap min is: 33
mHeap min is: 55
mHeap min is: 57
mHeap min is: 99
mHeap min is: 100
mHeap min is: 200
mHeap is returning numbers larger than k
mheap returned 420
adding 1 + 3
testing result: 4
adding 1 + 5
testing result: 6
adding 1 + 7
testing result: 8
adding 1 + 10
testing result: 11
adding 1 + 11
testing result: 12
adding 1 + 15
testing result: 16
adding 1 + 33
testing result: 34
adding 1 + 55
testing result: 56
adding 1 + 57
testing result: 58
adding 1 + 99
testing result: 100
adding 1 + 100
testing result: 101
adding 1 + 200
testing result: 201
adding 3 + 1
testing result: 4
adding 3 + 5
testing result: 8
adding 3 + 7
testing result: 10
adding 3 + 10
testing result: 13
adding 3 + 11
testing result: 14
adding 3 + 15
testing result: 18
adding 3 + 33
testing result: 36
adding 3 + 55
testing result: 58
adding 3 + 57
testing result: 60
adding 3 + 99
testing result: 102
adding 3 + 100
testing result: 103
adding 3 + 200
testing result: 203
adding 5 + 1
testing result: 6
adding 5 + 3
testing result: 8
adding 5 + 7
testing result: 12
adding 5 + 10
testing result: 15
adding 5 + 11
testing result: 16
adding 5 + 15
testing result: 20
adding 5 + 33
testing result: 38
adding 5 + 55
testing result: 60
adding 5 + 57
testing result: 62
adding 5 + 99
testing result: 104
adding 5 + 100
testing result: 105
adding 5 + 200
testing result: 205
adding 7 + 1
testing result: 8
adding 7 + 3
testing result: 10
adding 7 + 5
testing result: 12
adding 7 + 10
testing result: 17
adding 7 + 11
testing result: 18
adding 7 + 15
testing result: 22
adding 7 + 33
testing result: 40
adding 7 + 55
testing result: 62
adding 7 + 57
testing result: 64
adding 7 + 99
testing result: 106
adding 7 + 100
testing result: 107
adding 7 + 200
testing result: 207
adding 10 + 1
testing result: 11
adding 10 + 3
testing result: 13
adding 10 + 5
testing result: 15
adding 10 + 7
testing result: 17
adding 10 + 11
testing result: 21
adding 10 + 15
testing result: 25
adding 10 + 33
testing result: 43
adding 10 + 55
testing result: 65
adding 10 + 57
testing result: 67
adding 10 + 99
testing result: 109
adding 10 + 100
testing result: 110
adding 10 + 200
testing result: 210
adding 11 + 1
testing result: 12
adding 11 + 3
testing result: 14
adding 11 + 5
testing result: 16
adding 11 + 7
testing result: 18
adding 11 + 10
testing result: 21
adding 11 + 15
testing result: 26
adding 11 + 33
testing result: 44
adding 11 + 55
testing result: 66
adding 11 + 57
testing result: 68
adding 11 + 99
testing result: 110
adding 11 + 100
testing result: 111
adding 11 + 200
testing result: 211
adding 15 + 1
testing result: 16
adding 15 + 3
testing result: 18
adding 15 + 5
testing result: 20
adding 15 + 7
testing result: 22
adding 15 + 10
testing result: 25
adding 15 + 11
testing result: 26
adding 15 + 33
testing result: 48
adding 15 + 55
testing result: 70
adding 15 + 57
testing result: 72
adding 15 + 99
testing result: 114
adding 15 + 100
testing result: 115
adding 15 + 200
testing result: 215
adding 33 + 1
testing result: 34
adding 33 + 3
testing result: 36
adding 33 + 5
testing result: 38
adding 33 + 7
testing result: 40
adding 33 + 10
testing result: 43
adding 33 + 11
testing result: 44
adding 33 + 15
testing result: 48
adding 33 + 55
testing result: 88
adding 33 + 57
testing result: 90
adding 33 + 99
testing result: 132
adding 33 + 100
testing result: 133
adding 33 + 200
testing result: 233
adding 55 + 1
testing result: 56
adding 55 + 3
testing result: 58
adding 55 + 5
testing result: 60
adding 55 + 7
testing result: 62
adding 55 + 10
testing result: 65
adding 55 + 11
testing result: 66
adding 55 + 15
testing result: 70
adding 55 + 33
testing result: 88
adding 55 + 57
testing result: 112
adding 55 + 99
testing result: 154
adding 55 + 100
testing result: 155
adding 55 + 200
testing result: 255
adding 57 + 1
testing result: 58
adding 57 + 3
testing result: 60
adding 57 + 5
testing result: 62
adding 57 + 7
testing result: 64
adding 57 + 10
testing result: 67
adding 57 + 11
testing result: 68
adding 57 + 15
testing result: 72
adding 57 + 33
testing result: 90
adding 57 + 55
testing result: 112
adding 57 + 99
testing result: 156
adding 57 + 100
testing result: 157
adding 57 + 200
testing result: 257
RESULT IS : True
self.heap[0] : -9223372036854775807
minHeapify index: 2
minHeapify index: 1
 parent: 3 left: 7 right: 10
 parent: 7 left: 15 right: 0
mHeap min is: 3
mHeap min is: 15
mHeap min is: 10
mHeap min is: 7
adding 3 + 15
testing result: 18
adding 3 + 10
testing result: 13
adding 3 + 7
testing result: 10
adding 15 + 3
testing result: 18
adding 15 + 10
testing result: 25
adding 15 + 7
testing result: 22
adding 10 + 3
testing result: 13
adding 10 + 15
testing result: 25
adding 10 + 7
testing result: 17
RESULT IS : True
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
'''