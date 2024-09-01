class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        output = []
        i = 0
        while i < (len(s) // 2):
            s[left], s[right] = s[right], s[left]
            i += 1
            left += 1
            right -= 1
        return s