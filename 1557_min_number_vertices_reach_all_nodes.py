class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        # T: O(m), S: O(n)

        # Find all vertices that have parents in a set
        children = set()
        for p, c in edges:
            children.add(c)

        # Return vertices that have no parents
        return list(set([i for i in range(n)]) - children)
