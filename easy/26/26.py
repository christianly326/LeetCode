class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        if len(nums) == 0:
            return 0
        for r in range(len(nums) - 1):
            if nums[r] != nums[r + 1]:
                nums[l] = nums[r + 1]
                l += 1
        return l
# Time Complexity O(n)
# Space Complexity O(1)
            