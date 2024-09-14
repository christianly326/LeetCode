class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def helper(l, r, s):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            return "".join(s)
        self.ans = ''
        x = 2 * k
        s = list(s)
        if len(s) < k:
            l = 0
            r = len(s) - 1
            return helper(l, r, s)
        else:
            while len(s) > k:
                section = s[0:x]
                s = s[x:]
                change = section[0:k]
                rest = section[k:]
                l = 0
                r = len(change) - 1
                self.ans += helper(l, r, change) + "".join(rest)
            if len(s) <= k:
                l = 0
                r = len(s) - 1
                self.ans += helper(l, r, s)
        return self.ans
# Time complexity O(n)
# Space complexity O(n)