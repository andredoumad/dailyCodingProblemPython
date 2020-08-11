# Andre Doumad
'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns 
the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, 
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''

import unittest

class Solution(object):

    def solve(self, n):
        print('-------------')
        print('input: ', n)
        print('-------------')
        if len(n) <= 2:
            print('result: ')
            return max(0, max(n))

        max_excluding_last= max(0, n[0])
        print('max_excluding_last ', max_excluding_last)
        max_including_last = max(max_excluding_last, n[1])
        print('max_including_last ', max_including_last)
        print('n[2:] ', n[2:])
        for num in n[2:]:
            print(num)
            prev_max_including_last = max_including_last

            max_including_last = max(max_including_last, max_excluding_last + num)
            max_excluding_last = prev_max_including_last
        print('result: ')
        return max(max_including_last, max_excluding_last)

class unitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print(solution.solve([2,4,6,2,5]))
        print(solution.solve([5,1,1,5]))
        print(solution.solve([5,1,1,5,17,32,-2,0,-55,33,42,105,18]))


if __name__ == '__main__':
    unittest.main()


'''
-------------
input:  [2, 4, 6, 2, 5]
-------------
max_excluding_last  2
max_including_last  4
n[2:]  [6, 2, 5]
6
2
5
result: 
13
-------------
input:  [5, 1, 1, 5]
-------------
max_excluding_last  5
max_including_last  5
n[2:]  [1, 5]
1
5
result: 
10
-------------
input:  [5, 1, 1, 5, 17, 32, -2, 0, -55, 33, 42, 105, 18]
-------------
max_excluding_last  5
max_including_last  5
n[2:]  [1, 5, 17, 32, -2, 0, -55, 33, 42, 105, 18]
1
5
17
32
-2
0
-55
33
42
105
18
result: 
180
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

'''