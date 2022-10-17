from collections import deque
from math import dist


class Search():




        # solve_maze(maze)
    #must show coordinates in Tuple

    #def update_maze(self):
     #   maze =
    def __init__(self):
        self.maze = []
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.R, C = 0, 0
        self.end = ()
        self.start = ()

    def calc_euclidean(self,x, y):
        d = dist(x, y)
        return d

    def calc_manhattan(self,x, y):

        d = sum(abs(val1 - val2) for val1, val2 in zip(x, y))
        return d

    def astar(self,calc_dist):
        # Hn gives us estimate from node N to END (HEURISTIC FUNCTION)
        # Gn is the current shortest distance from start node to current node
        # Fn = Gn + Hn
        open = []
        open.append((self.start[0], self.start[1], 0, calc_dist(self.start, self.end)))

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
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == "%" or visited[nr][nc]): continue
                h = calc_dist(x, self.end)
                g = calc_dist(x, self.start)
                f = h + g
                open.append((nr, nc, coord[2] + 1, f))

                if self.maze[nr][nc] == "G":
                    print(nr, nc)
                    return coord[2]

        return "Unable to find Goal"

    def greedy(self,calc_dist):
        # Place Starting Node into the Open List
        open = []
        open.append((self.start[0], self.start[1], 0, calc_dist(self.start, self.end)))

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
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == "%" or visited[nr][nc]): continue
                z = calc_dist(x, self.end)
                open.append((nr, nc, coord[2] + 1, z))

                if self.maze[nr][nc] == "G":
                    print(nr, nc)
                    return coord[2]

        return "Unable to find Goal"

    # How do i translate depth d from integer to coordinates

    def start_DFS_helper(self,maze, R, C, start, d):
        queue = deque()
        queue.append((start[0], start[1], 0))

        visited = [[False] * C for _ in range(R)]

        for _ in range(2 ** d):
            coord = queue.pop()
            visited[coord[0]][coord[1]] = True
            # print(coord)
            if maze[coord[0]][coord[1]] == "G":
                return coord[2], True

            for dir in self.directions:
                nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "%" or visited[nr][nc]): continue
                queue.append((nr, nc, coord[2] + 1))

        return "not found", False

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
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == "%" or visited[nr][nc]): continue
                stack.append((nr, nc, coord[2] + 1))

    def iterative(self):
        d = 1
        found = False
        coord = (0, 0)
        while found == False:
            coord, found = self.start_DFS_helper(self.maze, self.R, self.C, self.start, d)
            d += 1
            print(d)
        print("this is where the G is located", coord)



    # Given a maze find the shortest path