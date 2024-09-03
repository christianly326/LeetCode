# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        mid = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            print(left, mid, right)
            if left == right:
                return mid
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

            