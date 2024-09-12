class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for n in logs:
            if n == "../" and stack:
                stack.pop()
            elif n == "./" or n == "../":
                continue
            else:
                stack.append(n)
        return len(stack)
    
#Time complexity O(n)
#Space complexity O(n) In the Worst case
