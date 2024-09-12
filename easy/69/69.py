class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + ((right - left) // 2)
            pos = mid * mid
            if pos == x:
                return mid
            elif x < pos:
                right = mid - 1
            else:
                left = mid + 1
        return right

# Time Complexity O(log(x))
# Space Complexity O(1)