class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        build = 0
        check = False
        if x < 0:
            check = True
            x = abs(x)
        while x > 0:
            digit = x % 10
            x //= 10
            build *= 10
            build += digit
            i += 1
        
        if check:
            if -build < (-2 ** 31):
                return 0
            return -build
        if build > (2 ** 31) - 1:
            return 0
        return build
# time complexity O(log to the base of 10 (x))
# Space complexity O(1)