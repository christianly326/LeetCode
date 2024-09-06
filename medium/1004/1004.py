class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        max_len = 0
        flipped = 0
        for r in range(n):
            if nums[r] == 0:
                flipped += 1
            while flipped > k:
                if nums[left] == 0:
                    flipped -= 1
                left += 1
            length = r - left + 1
            max_len = max(max_len, length)
        return max_len
#Time Complexity O(n)
# Space complexity O(1)