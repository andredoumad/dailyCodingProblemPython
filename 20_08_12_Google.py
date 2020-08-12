# Andre Doumad
#TODO find path after first DFS pass
'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
import time
class Graph():
    def __init__(self):
        self.adjecencyMatrix = {}
        self.startV = 0
        self.startE = 0
        self.endV = 0
        self.endE = 0

    # add v e
    def addEdge(self, v, e):
        if v in self.adjecencyMatrix:
            self.adjecencyMatrix[v].append(e)
        else:
            self.adjecencyMatrix[v] = [e]

    # set start and end
    def setStartEnd(self, start, end):
        self.startV = start[0]
        self.startE = start[1]
        self.endV = end[0]
        self.endE = end[1]

    # breadth first search
    def bfs(self):
        adj = self.adjecencyMatrix
        return self.doBfs(self.startV, [self.startV], {self.startV:True}, adj)

    def doBfs(self, start, queue, visited, adj):

        edgeLists = [] 
        while len(queue) > 0:
            print('------')
            print('queue is: ', queue)
            v = queue.pop(0)
            edges = []
            while len(adj[v]) > 0:
                e = adj[v].pop()
                edges.append(e)
                if e not in visited:
                    visited[e] = True
                    queue.append(e)
            edgeLists.append(edges)
            print('edges ', edges)
            print('visited ', visited)
            print('paths available for ', v, ' is ', len(edges))
            del adj[v]
            # time.sleep(1)

        steps = 1
        nextEdge = 0
        prevEdge = 0
        matchingEdges = 0
        for a in range(0, len(edgeLists)-1):
            print('+++++')
            print('edgeLists[a] ',edgeLists[a])
            print('edgeLists[a+1] ',edgeLists[a+1])
            matches = []
            for b in range(0, len(edgeLists[a])):
                for c in range(0, len(edgeLists[a+1])):
                    if edgeLists[a][b] == edgeLists[a+1][c]:
                        matches.append(edgeLists[a][b])
            print('matches ', matches)
            if len(matches) == 0:
                return 'No path to end :('
            steps += min(matches)
            prevEdge = min(matches)
            print('prevEdge ', prevEdge)
            if self.startV == a:
                break
        if prevEdge > self.endE:
            steps += prevEdge
        elif prevEdge < self.endE:
            distance = self.endE - prevEdge
            steps += distance


        print(steps)
        return steps



    # print graph
    def printGraph(self):
        for k,v in self.adjecencyMatrix.items():
            print('k ', k, ' v ', v)
        print('start: v', self.startV, ' e ',self.startE )
        print('end: v', self.endV, ' e ', self.endE )

class Solution():
    def solve(self, matrix):
        graph = Graph()
        for a in range(0,len(matrix)):
            for b in range(0,len(matrix)):
                if matrix[a][b] == False:
                    graph.addEdge(a,b)

        graph.setStartEnd([3,0],[0,0])
        graph.printGraph()
        return graph.bfs()
            


solution = Solution()
result = solution.solve([[False, False, False, False],
                [True, True, False, True],
                [False, False, False, False],
                [False, False, False, False]])

print('result: ', result)