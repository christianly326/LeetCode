class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        point = len(digits) - 1
        x = digits[point]
        while x == 9 and point >= 0:
            digits[point] = 0
            point -= 1
            x = digits[point]
        
        if point >= 0:
            digits[point] += 1
        else:
            digits.append(0)
            for i in range(len(digits)):
                if i == 0:
                    digits[i] = 1
                else:
                    digits[i] = 0
        return digits
# Time complexity O(n)
# Space complexity O(1)