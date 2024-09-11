class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ord('a') - 1
        total = 0
        for n in s:
            num = ord(n) - a
            print(num)
            while num > 0:
                digit = num % 10
                num //= 10
                total += digit
        while k > 1:
            new = 0
            while total > 0:
                digit = total % 10
                total //= 10
                new += digit
            print(new)
            total = new
            k -= 1
        return total
# Space compleixty O(n)
# Time Complexity O(n + k)