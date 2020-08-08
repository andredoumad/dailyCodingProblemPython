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
    def __init__(self):
        self.colors = ['red', 'green', 'blue', 'yellow']

    def arrangeColors(self, houseCosts):
        houseColors = {}
        previousColorIndex = None
        for k,v in houseCosts.items():
            print('house[', k, ' color costs = ' + str(v))
            cheapestColorPrice = max(v) + 1
            cheapestIndex = 0
            for i in range(0, len(v)):
                if previousColorIndex == None and v[i] < cheapestColorPrice:
                    cheapestColorPrice = v[i]
                    cheapestIndex = i
                elif previousColorIndex != None and v[i] < cheapestColorPrice and i != previousColorIndex:
                    cheapestColorPrice = v[i]
                    cheapestIndex = i
            print('cheapest color is: ', self.colors[cheapestIndex], ' cost is ', cheapestColorPrice)
            houseColors[k] = cheapestIndex
            previousColorIndex = cheapestIndex
        
        previousColorIndex = None
        previousKey = 0
        for k,v in houseColors.items(): 
            print('house ', k, ' is ', self.colors[v])
            if previousColorIndex == None:
                previousColorIndex = v
            else:
                if previousColorIndex == v:
                    print('two of the same colors in a row!')
                    # based on the previous house and this house, 
                    # choose the next cheapest color between them
                    exit()
            previousColorIndex = v
            previousKey = k
        return houseColors

    def solve(self, houseMatrix=None):
        houseCosts = {}
        
        # populate houseCosts dict
        for a in range(0, len(houseMatrix)):
            for b in range(0, len(houseMatrix[a])):
                if b not in houseCosts:
                    houseCosts[b] = [houseMatrix[a][b]]
                else:
                    houseCosts[b].append(houseMatrix[a][b])
        
        result = self.arrangeColors(houseCosts)
        return result

class UnitTest(unittest.TestCase):
    
    def test_a(self):
        solution = Solution()

        houseMatrix = [
    # houses 0,1,2,3,4,5,6
            [3,7,2,4,6,5,2], # red
            [9,3,3,8,3,7,5], # green
            [1,2,5,3,8,3,9], # blue
            [5,2,1,7,4,5,8]  # yellow
            ]

        solution.solve(houseMatrix)

if __name__=='__main__':
    unittest.main()

'''
OUTPUT:
house[ 0  color costs = [3, 9, 1, 5]
cheapest color is:  blue  cost is  1
house[ 1  color costs = [7, 3, 2, 2]
cheapest color is:  yellow  cost is  2
house[ 2  color costs = [2, 3, 5, 1]
cheapest color is:  red  cost is  2
house[ 3  color costs = [4, 8, 3, 7]
cheapest color is:  blue  cost is  3
house[ 4  color costs = [6, 3, 8, 4]
cheapest color is:  green  cost is  3
house[ 5  color costs = [5, 7, 3, 5]
cheapest color is:  blue  cost is  3
house[ 6  color costs = [2, 5, 9, 8]
cheapest color is:  red  cost is  2
house  0  is  blue
house  1  is  yellow
house  2  is  red
house  3  is  blue
house  4  is  green
house  5  is  blue
house  6  is  red
'''