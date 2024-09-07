class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        l = 0
        n = len(nums)
        maxCount = 0
        for r in range(n):
            table[nums[r]] = table.get(nums[r], 0) + 1
            length = r - l
            if length > k:
                table[nums[l]] -= 1
                l += 1
            maxCount = max(maxCount, table[nums[r]])
            if maxCount == 2:
                return True
        return False
# Space Complexity O(n)
# Time Complexity O(n)  