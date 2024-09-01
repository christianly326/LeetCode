class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([n.lower() for n in s if n.isalnum()])
        left = 0
        right = len(new_s) - 1
        while left < (len(new_s) // 2):
            if new_s[left] != new_s[right]:
                print(new_s[left], new_s[right])
                return False
            left += 1
            right -= 1
        return True