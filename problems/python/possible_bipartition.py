from collections import deque, defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list) # adjacency list of the graph

        for i in range(len(dislikes)):
            a, b = dislikes[i]
            graph[a].append(b)
            graph[b].append(a)

        colors = {}  # color of each element of the graph : 0 no color, -1 blue, 1 red
        
        def bfs(node):    # bfs algorithm from a starting node
            queue = deque([node])  # initalize the queue
            colors[node] = 1   # initialize the color as red 
            while queue:  # while the queue is not empty
                p = queue.popleft()
                cur_color = colors[p]
                for neigh in graph[p]:
                    if neigh in colors and colors[neigh] == cur_color:  # if a neighbor has the same color, we return False
                        return False
                    elif neigh in colors and colors[neigh] == -cur_color:  # else we set the neighbor color as the opposite of the current node
                        continue
                    colors[neigh] = -cur_color
                    queue.append(neigh)
            return True
        
        for i in range(1, n+1):
            if i not in colors:   # if the point has no color, it is not visited
                if not bfs(i):
                    return False
        
        return True