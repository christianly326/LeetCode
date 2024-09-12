class Solution:
    def countSeniors(self, details: List[str]) -> int:
        x = 11
        y = 13
        count = 0
        for n in details:
            age  = int(n[x:y])
            if age > 60:
                count += 1
        return count
# Time complexity O(n)
# Space complexity O(1)