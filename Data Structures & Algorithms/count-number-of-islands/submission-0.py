class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        def dfs(node):
            if node[0] < 0 or node[0] >= len(grid):
                return
            if node[1] < 0 or node[1] >= len(grid[node[0]]):
                return
            if node in visited or grid[node[0]][node[1]] == '0':
                return
            if grid[node[0]][node[1]] == '1':
                visited.add(node)
            for x, y in directions:
                temp = list(node)
                temp[0] += x
                temp[1] += y
                dfs(tuple(temp))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs((i,j))
                    islands += 1
        return islands
            
        