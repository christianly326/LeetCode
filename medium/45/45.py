class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return 0
        maxReach = nums[0]
        jumpCount = 1
        end = nums[0]
        for i in range(1, n):
            if i == n - 1:
                return jumpCount
            maxReach = max(maxReach, i + nums[i])
            if i == end:
                jumpCount += 1
                end = maxReach
            if end >= n - 1:
                return jumpCount
        


# Time complexity O(n)
# Space complexity O(1)