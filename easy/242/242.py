class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for n in s:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
        for m in t:
            if m in table:
                table[m] -= 1
            else:
                return False
        for k, v in table.items():
            if v != 0:
                return False
        return True


