class Solution:
    def climbStairs(self, n: int) -> int:
        def recursion(n, cache={}):
            if n <= 1:
                return n
            if n not in cache:
                cache[n] = recursion(n-1) + recursion(n-2)
            return cache[n]
        return recursion(n + 1)