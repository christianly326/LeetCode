class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sett = set()
        l = 0
        n = len(s)
        max_count = 0
        count = {}
        max_length = 0
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(count.values())
            length = r - l + 1
            if length - max_count > k:
                count[s[l]] -= 1
                l += 1
            new_length = r - l + 1
            max_length = max(max_length, new_length)
        return max_length
# Space Complexity O(n)
# Time Complexity O(n)
