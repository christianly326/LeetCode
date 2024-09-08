class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = ''
        stack = []
        s = path.split('/')
        for n in s:
            if n == '.' or n == '':
                continue
            elif n == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        print(stack)
        return ("/"+"/".join(stack))
#Time Complexity O(n)
#Space Complexity O(n)
            