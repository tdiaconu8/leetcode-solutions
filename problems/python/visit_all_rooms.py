from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        graph = {i: rooms[i] for i in range(n)}  # graph to map rooms to keys
        
        queue = deque([0])  # queue to store the rooms we need to visit
        vis = set()  # set to store the visited rooms

        while queue:
            r = queue.popleft()  # we go to the next room to visit
            vis.add(r)  # add the room to the visited set
            if len(vis) == n:  # if we visited all the rooms we return True
                return True
            for neigh in graph[r]:
                if neigh not in vis:  # we add the neighbors to next rooms to visit
                    queue.append(neigh)
        
        return False