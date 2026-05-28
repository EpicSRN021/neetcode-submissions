class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        clear = set()
        for c, p in prerequisites:
            if c not in adj:
                adj[c] = [p]
            else:
                adj[c].append(p)
        def dfs(course, visited):
            if course not in adj:
                return True
            if course in visited:
                return False
            visited.add(course)
            for c in adj[course]:
                if c in clear:
                    continue
                if dfs(c, visited) == False:
                    return False
            visited.remove(course)
            clear.add(course)
            return True
        for c in adj:
            visited = set()
            if dfs(c, visited) == False:
                return False
        return True

        