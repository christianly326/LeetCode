class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": int.__add__,
            "-": int.__sub__,
            "*": int.__mul__,
            "/": int.__truediv__,
        }
        stack = []
        for n in tokens:
            if n in ops:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(ops[n](b, a))
            else:
                stack.append(n)
        return int(stack.pop())
