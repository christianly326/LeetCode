class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_to_jewels = {}
        for n in jewels:
            stones_to_jewels[n] = 1
        total = 0
        for stone in stones:
            if stone in stones_to_jewels:
                total += stones_to_jewels[stone]
        return total