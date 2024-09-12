class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sett = set(allowed)
        count = 0
        for n in words:
            count += 1
            for m in n:
                if m not in sett:
                    count -= 1
                    break
        return count
# Time complexity O(n * m)
# Space complexity O(x) where x is the number of allowed letters