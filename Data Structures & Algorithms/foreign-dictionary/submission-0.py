class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                adj[words[i][j]] = set()
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i-1]):
                if j == len(words[i]):
                    return ""
                if words[i-1][j] != words[i][j]:
                    adj[words[i-1][j]].add(words[i][j])
                    break
                j += 1
        #False if in current path and True if we know path is valid
        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = False
            for c in adj[char]:
                if not dfs(c):
                    return False
            visited[char] = True
            res.append(char)
            return True
        for c in adj:
            if not dfs(c):
                return ""
        return "".join(res[::-1])

            
        