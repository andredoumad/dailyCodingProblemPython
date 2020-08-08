# Andre Doumad
'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the 
cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''
import unittest


class Solution(object):
    
    def solve(self, houseMatrix=None):
        houseCosts = {}
        # populate houseCosts dict
        for a in range(0, len(houseMatrix)):
            for b in range(0, len(houseMatrix[a])):
                print('house[', a, '] color[', b, '] costs: ', houseMatrix[a][b])
                if a not in houseCosts:
                    houseCosts[a] = [houseMatrix[a][b]]
                else:
                    houseMatrix[a].append([houseMatrix[a][b]])

        for k,v in houseCosts:
            # houseCosts[k] = sorted(v)
            print('house[', k, ' color costs = ', v)

        print(houseCosts)

        houseAdj = {}
        houseColors = {}
        # based on cost and house adjacency matrix choose color

class UnitTest(unittest.TestCase):
    
    def test_a(self):
        solution = Solution()

        houseMatrix = [
    # houses 1,2,3,4,5,6,7
            [3,7,2,4,6,5,2], # red
            [9,3,3,8,4,7,5], # green
            [1,2,5,3,1,3,9], # blue
            [5,2,1,7,4,5,8]  # yellow
            ]

        solution.solve(houseMatrix)

if __name__=='__main__':
    unittest.main()