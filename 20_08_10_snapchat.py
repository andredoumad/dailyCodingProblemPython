# Andre Doumad
'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for 
classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

class Solution(object):
    def solve(self, n):
        times = {}
        maxOverlapping = 0
        n = sorted(n)
        for a in range(0,len(n)-1):
            overlapping = 0
            for b in range(1, len(n)):
                if max(n[a]) >= min(n[a+1]):
                    overlapping += 1
            if overlapping > maxOverlapping:
                maxOverlapping = overlapping
        return maxOverlapping

solution = Solution()
result = solution.solve([(30, 75), (0, 50), (60, 150)])
print('result is ', result)

'''
output:
result is  2
'''