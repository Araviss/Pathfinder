import queue
from collections import deque


import heuristic


class Search():


    def __init__(self):
        self.maze = []
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.R, C = 0, 0
        self.end = ()
        self.start = ()
        self.fifo = deque()
        self.heuristic = heuristic.Heuristics()
        self.wallList = []


    def get_wall_list(self):
        return self.wallList

    def get_start(self):
        return self.start


    def get_end(self):
        return self.end

    def updateWall(self, r, c):
        self.wallList.append((r,c))

    def set_start(self, start):
        self.start = start


    def set_end(self, end):
        self.end = end



    # Currently uses the euclidean formula to calculate the
    # distance between the beginning and end points
    # Eventually would like to be able to switch between
    # Manhattan and Euclidean in the UI
    def astar(self):
        # Hn gives us estimate from node N to END (HEURISTIC FUNCTION)
        # Gn is the current shortest distance from start node to current node
        # Fn = Gn + Hn
        open = []
        d = self.heuristic.calc_euclidean(self.start, self.end)
        open.append((self.start[0], self.start[1], 0, d))

        # Initializes all grid elements as unvisited
        visited = [[False] * self.C for _ in range(self.R)]

        # Continue searching while stack is not empty
        while len(open) != 0:
            try:
                i = 0
                j = 0
                # Find lowest z value in list
                for c in range(len(open) - 1):
                    elem = open[c]
                    elem2 = open[c + 1]
                    #Determines if distance of elem is less than distance of elem2
                    if elem[3] < elem2[3]:
                        i = elem[3]
                        j = elem
                coord = j
                open.remove(coord)
                visited[coord[0]][coord[1]] = True
            except:
                coord = open.pop()
                visited[coord[0]][coord[1]] = True

            for dir in self.directions:
                nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                x = (nr, nc)
                if (nr < 0 or nr >= self.R
                        or nc < 0
                        or nc >= self.C
                        or self.maze[nr][nc] == "X"
                        or visited[nr][nc]):
                    continue

                h = self.heuristic.calc_manhattan(x, self.end)
                g = self.heuristic.calc_manhattan(x, self.start)
                f = h + g
                open.append((nr, nc, coord[2] + 1, f))

                if self.maze[nr][nc] == "G":
                    print(nr, nc)
                    self.fifo.pop()
                    return coord[2]
                self.fifo.append((nr,nc))

        return "Unable to find Goal"

    def greedy(self):
        # Place Starting Node into the Open List
        open = []
        open.append((self.start[0], self.start[1], 0, self.heuristic.calc_euclidean(self.start, self.end)))

        visited = [[False] * self.C for _ in range(self.R)]

        # Contnue searching while stack is not empty
        while len(open) != 0:
            try:
                i = 0
                j = 0
                # Find lowest z value in list
                for c in range(len(open) - 1):
                    elem = open[c]
                    elem2 = open[c + 1]
                    if elem[3] < elem2[3]:
                        i = elem[3]
                        j = elem
                coord = j
                open.remove(coord)
                visited[coord[0]][coord[1]] = True
            except:
                coord = open.pop()
                visited[coord[0]][coord[1]] = True

            for dir in self.directions:
                nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                x = (nr, nc)
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == "X" or visited[nr][nc]): continue
                z = self.heuristic.calc_euclidean(x, self.end)
                open.append((nr, nc, coord[2] + 1, z))

                if self.maze[nr][nc] == "G":
                    print(nr, nc)
                    self.fifo.pop()
                    return coord[2]
                self.fifo.append((nr,nc))

        return "Unable to find Goal"

    #Depth First search that help Iterative
    def start_DFS_helper(self,maze, R, C, start, d):
        #Continues to try as long as there's something in queue
        try:
            queue = deque()
            queue.append((start[0], start[1], 0))
            visited = [[False] * C for _ in range(R)]

            for _ in range(2 ** d):
                coord = queue.pop()
                visited[coord[0]][coord[1]] = True
                # print(coord)
                if maze[coord[0]][coord[1]] == "G":
                    return ([coord[0]],[coord[1]]), 1

                for dir in self.directions:
                    nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                    if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "X" or visited[nr][nc]): continue
                    queue.append((nr, nc, coord[2] + 1))
                    if (nr,nc)  not in self.fifo:
                        self.fifo.append((nr,nc))
        #Catches when queue is empty. This means couldn't find Goal
        except:
            return "not found ", -1
        #Still has more squares to search but wasn't found at current depth
        return "not found yet", 0

    def depth_first(self):
        stack = deque()
        stack.append((self.start[0], self.start[1], 0))

        visited = [[False] * self.C for _ in range(self.R)]

        while len(stack) != 0:
            coord = stack.pop()
            visited[coord[0]][coord[1]] = True

            if self.maze[coord[0]][coord[1]] == "G":
                print(coord[2])
                return coord[2]

            for dir in self.directions:
                nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == "X" or visited[nr][nc]): continue
                stack.append((nr, nc, coord[2] + 1))
                self.fifo.append((nr, nc))

    def iterative(self):
        d = 1
        found = 0
        coord = (0, 0)
        while found == 0:
            coord, found = self.start_DFS_helper(self.maze, self.R, self.C, self.start, d)
            d += 1
            print(d)
        print("this is where the G is located", coord)



#VISUALIZE THE ITERATIVE FUNCTION