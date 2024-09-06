class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        max_average = 0
        total = 0
        n = len(nums)
        for i in range(k):
            total += nums[i]
        max_average = total / k
        for i in range(k, n):
            total += nums[i]
            total -= nums[i-k]

            curr_average = total / k
            max_average = max(max_average, curr_average)
        return max_average
# Space Complexity O(1)
# Time Complexity O(n)
