class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        while n != 1:
            if n in sett:
                print(n, sett)
                return False
            else:
                sett.add(n)
            sum_square = 0
            while n > 0:
                sum_square += (n % 10) * (n % 10)
                n //= 10
            n = sum_square
        return True

