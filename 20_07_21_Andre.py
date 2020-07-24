# Andre Doumad
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
# We will be sending the solution tomorrow, along with tomorrow's question.

import unittest

class Solution(object):
    def __init__(self):
        self.numbers = [10, 15, 3, 7]
        self.k = 17

    def solve(self):

        for i in range(0, len(self.numbers)):
            a = self.numbers[i]
            for j in range(0, len(self.numbers)):
                if j != i:
                    b = self.numbers[j]
                    print('adding ' + str(a) + ' + ' + str(b))
                    result = a+b
                    print('testing result: ' + str(result))
                    if b + a == self.k:
                        return True
        return False




class unitTest(unittest.TestCase):
    def test_0(self):
        solution = Solution()
        
        result = solution.solve()
        print('RESULT IS : ' + str(result))
        self.assertTrue(solution.solve, "return true since 10 + 7 is 17.")

if __name__ == '__main__':
    unittest.main()