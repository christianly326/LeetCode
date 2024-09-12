class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def decimal_convert(bit: str):
            total = 0
            n = len(bit)
            for i in bit:
                n -= 1
                total += int(i) * (2 ** n)
            return total
        change = decimal_convert(a) + decimal_convert(b)
        bit = ''
        if change == 0:
            return a
        while change > 0:
            bit += str(change % 2)
            change //= 2
        bit = bit[::-1]
        return bit
        
                