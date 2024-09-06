class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l = 1
        count = 1
        for r in range(1, len(nums)):
            if nums[r] == nums[r - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[l] = nums[r]
                l += 1
        return l
# Time Complexity O(n)
# Space Complexity O(1)
            