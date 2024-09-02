class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == 'D':
                peek = stack[-1]
                stack.append(peek * 2)
            elif operation == '+':
                a = stack[-1]
                b = stack[-2]
                c = a + b
                stack.append(c)
            else:
                stack.append(int(operation))
            print(stack)
        total = 0
        for n in stack:
            total += n
        return total