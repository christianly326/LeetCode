class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        print(r)
        while r >= 0 and s[r] != " ":
            count += 1
            r -= 1
        return count
# Time complexity O(n)
# Space complexity O(1)