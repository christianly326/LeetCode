class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        requirement = len(nums) / 2
        for n in nums:
            table[n] = table.get(n, 0) + 1
        for k, v in table.items():
            if v > requirement:
                return k