class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = list(word)
        path = set()
        def dfs(x, y, i):
            if i == len(target):
                return True
            if x < 0 or x == len(board) or y < 0 or y == len(board[x]) or (x,y) in path:
                return False
            path.add((x,y))
            if board[x][y] == target[i]:
                if (
                    dfs(x-1, y, i+1) or 
                    dfs(x+1, y, i+1) or
                    dfs(x, y-1, i+1) or
                    dfs(x, y+1, i+1)
                ):
                    return True
            path.remove((x,y))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
            
        