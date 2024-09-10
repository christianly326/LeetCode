class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        output = [i for i in nums]
        for r, n in enumerate(output):
            position = ((k + r) % len(nums))
            nums[position] = n
        return