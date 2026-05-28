class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for idx, i in enumerate(strs):
            temp = "".join(sorted(i))
            if temp in s:
                s[temp].append(i)
            else:
                s[temp] = [i]
        f = []
        for i in s:
            f.append(s[i])
        return f


        