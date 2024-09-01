class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        i = 0
        while i < len(nums):
            x = nums[i]
            y = target - nums[i]
            if y in table:
                return [table[y], i]
            table[x] = i
            i += 1
        return [] #assuming theres no solution
            
                