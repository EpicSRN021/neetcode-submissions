class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False
            else:
                stack.append(i)
        return not stack
