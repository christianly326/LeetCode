class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num - 1
        if num == 1:
            return True
        while left <= right:
            mid = left + ((right - left) // 2)
            if (mid * mid) == num:
                return True 
            if (mid * mid) < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
