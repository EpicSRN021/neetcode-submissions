from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Recursive Approach
        # @cache
        # def dfs(l, r):
        #     if l < 0 or r < 0:
        #         return 0
        #     if text1[l] == text2[r]:
        #         return 1 + dfs(l-1, r-1)
        #     else:
        #         return max(dfs(l-1, r), dfs(l, r-1))

        # return dfs(len(text1) - 1, len(text2) - 1)

        # dp = []
        # for i in range(len(text1)+1):
        #     temp = []
        #     for j in range(len(text2)+1):
        #         temp.append(0)
        #     dp.append(temp)
        dp = [[0] * (len(text2)+1) for i in range(len(text1)+1)]
        for i in range(1, len(text1)+ 1):
            for j in range(1, len(text2) + 1):
                if text1[i -1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)][len(text2)]

            
