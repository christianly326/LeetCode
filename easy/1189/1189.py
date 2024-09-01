class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        table = {}
        ans = float('inf')
        for n in target:
            table[n] = 0
        for m in text:
            if m in table:
                table[m] += 1
        table['l'] = table['l'] // 2   
        table['o'] = table['o'] // 2   
        for v in table.values():
            if v < ans:
                ans = v
        return ans
