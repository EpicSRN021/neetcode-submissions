from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(l, r):
            if l < 0 or r < 0:
                return 0
            if text1[l] == text2[r]:
                return 1 + dfs(l-1, r-1)
            else:
                return max(dfs(l-1, r), dfs(l, r-1))
                
        return dfs(len(text1) - 1, len(text2) - 1)
            
