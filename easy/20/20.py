class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in s:
            if not stack:
                stack.append(n)
                continue
            if n == '}':
                if stack.pop() != "{":
                    return False
            elif n == ']':
                if stack.pop() != "[":
                    return False
            elif n == ')':
                if stack.pop() != "(":
                    return False
            else:
                stack.append(n)
        return not stack
# Time complexity O(n)
# Space complexity O(n)
