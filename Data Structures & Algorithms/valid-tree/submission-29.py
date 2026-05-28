class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        clear = set()
        # if len(edges) != n-1:
        #     return False
        # if n == 1:
        #     return True
        for l, r in edges:
            if l not in adj:
                adj[l] = [r]
            else:
                adj[l].append(r)
            if r not in adj:
                adj[r] = [l]
            else:
                adj[r].append(l)
        def dfs(course, visited, prev):
            if course in visited:
                return False
            visited.add(course)
            if course not in adj:
                return False
            for c in adj[course]:
                if c == prev:
                    continue
                if c in clear:
                    continue
                if dfs(c, visited, course) == False:
                    return False
            clear.add(course)
            return True

        visited = set()
        if edges == []:
            return True
        if dfs(0, visited, None) == False or len(visited) != n:
            return False
        return True

































        
        