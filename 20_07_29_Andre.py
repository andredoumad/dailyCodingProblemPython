'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''

import unittest

class Solution(object):

    def solve(self, n):
        print('--------------')
        return self.solveIt(n, 0, [], False)

    def solveIt(self, n, total, sums, left):
        print('total ', total)
        print('sums ', sums)
        lOfN = len(n)
        while lOfN >= 2:
            lOfN -= 1
            if n[lOfN-1] < n[lOfN]:
                sums.append(n[lOfN])
                total+= n[lOfN]
                n.pop()
                n.pop()
                return self.solveIt(n, total, sums, False)
            else:
                sums.append(n[lOfN-1])
                total+= n[lOfN-1]
                n.pop()
                n.pop()
                return self.solveIt(n, total, sums, True)
        if len(n) == 1 and left == False:
            total += n[0]
        return total


class unitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print(solution.solve([2,4,6,2,5]))
        print(solution.solve([5,1,1,5]))
        print(solution.solve([5,1,1,5,17,32,-2,0,-55,33,42,105,18]))


if __name__ == '__main__':
    unittest.main()


'''
OUTPUT:


--------------
total  0
sums  []
total  5
sums  [5]
total  11
sums  [5, 6]
13
--------------
total  0
sums  []
total  5
sums  [5]
total  10
sums  [5, 5]
10
--------------
total  0
sums  []
total  105
sums  [105]
total  147
sums  [105, 42]
total  147
sums  [105, 42, 0]
total  179
sums  [105, 42, 0, 32]
total  196
sums  [105, 42, 0, 32, 17]
total  197
sums  [105, 42, 0, 32, 17, 1]
197

'''