class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for num in adj[n]:
                dfs(num)
        
        res = n
        for i in range(n):
            if i in visited:
                res -= 1
            else:
                dfs(i)
        return res
        