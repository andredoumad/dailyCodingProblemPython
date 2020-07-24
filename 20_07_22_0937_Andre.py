# Andre Doumad
# Daily Coding Problem: Problem #2 [Hard]

# This problem was asked by Uber.

# Given an array of integers, 
# return a new array such that each element at index i of 
# the new array is the product of all the numbers 
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


import unittest, time

# solution
class Solution(object):
    def solve(self, a):
        result = [0]*len(a)
        # print(result)
        for i in range(0, len(a)):
            # print(a[i])
            # nums = []
            # print('-------------')
            product = 1
            for k in range(0, len(a)):
                if i != k:
                    # print('a[k]=' + str(a[k]))
                    product = product * a[k]
                    # print('product=' + str(product))
            result[i] = product
            # print(result)
        return result

# unittest
class unitTest(unittest.TestCase):
    def test_0(self):
        # print('test_0')
        solution = Solution()
        startTime = time.time()
        result = solution.solve([1, 2, 3, 4, 5])
        print('time: ' + str(time.time()-startTime))

        # print('RESULT: ' + str(result))
        # self.assertEqual(result, [120, 60, 40, 30, 24], 'result should equal [120, 60, 40, 30, 24]')
        pass

if __name__ == '__main__':
    print('unittest')
    unittest.main()