from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.visited_nodes = {}
        self.island_count = 0
        rows, cols = len(grid), len(grid[0])
        
        def traverseNeighbours(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                (i, j) in self.visited_nodes or grid[i][j] == "0"):
                return
            
            self.visited_nodes[(i, j)] = True
            # Traverse in all four directions
            traverseNeighbours(i + 1, j)
            traverseNeighbours(i - 1, j)
            traverseNeighbours(i, j + 1)
            traverseNeighbours(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in self.visited_nodes and grid[i][j] == "1":
                    self.island_count += 1
                    traverseNeighbours(i, j)
        
        return self.island_count
