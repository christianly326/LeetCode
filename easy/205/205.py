class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        seen = set()
        if len(s) != len(t):
            return False
        for i, n in enumerate(s):
            if n not in table:
                if t[i] in seen:
                    return False
                table[n] = t[i]
                seen.add(t[i])
            elif table[n] != t[i]:
                    return False
        return True  
# Time Complexity O(n)
# Space Complexity O(n)