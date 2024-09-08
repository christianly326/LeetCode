class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        seen = set()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i, n in enumerate(pattern):
            if n in table:
                if table[n] != s[i]:
                    return False
            else:
                if s[i] in seen:
                    return False
                table[n] = s[i]
                seen.add(s[i])
        return True
# Space Complexity O(n)
# Time Complexity O(n)