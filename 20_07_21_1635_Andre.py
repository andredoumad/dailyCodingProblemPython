# Andre Doumad
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
# We will be sending the solution tomorrow, along with tomorrow's question.
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