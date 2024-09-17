class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        table = {
            "{" : "}",
            "[" : "]",
            "(" : ")",
        }
        stack = []
        x = []
        check = True
        for n in s:
            if n in table.values() and stack:
                p = stack.pop()
                if table[p] != n:
                    check = False
            elif n in table.values() and len(stack) == 0:
                check = False
            if n in table.keys():
                stack.append(n)
            if check:
                x.append(n)
            check = True
        i = 0
        m = len(stack)
        while m > 0:
            if x[-i - 1] in table.keys():
                x[-i - 1] = ''
                m -= 1
            i += 1
        return "".join(x)
# Time complexity O(n)
# Space complexity O(n)
