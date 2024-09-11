class Solution:
    def findComplement(self, num: int) -> int:
        bit = ''
        while num > 0:
            bit += '0' if num % 2 == 1 else '1'
            num //= 2
        exp = 0
        total = 0
        for n in bit:
            num = int(n) * (2 ** exp)
            exp += 1
            total += num
        return total
# Time complexity O(log n)
# Space complexity O(log n)
