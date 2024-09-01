class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for n in ransomNote:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
        for n in magazine:
            if n in table:
                table[n] -= 1
        for k, v in table.items():
            if v > 0:
                return False
        return True