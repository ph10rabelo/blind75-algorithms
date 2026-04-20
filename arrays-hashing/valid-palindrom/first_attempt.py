import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s[::-1]
        reverse = re.sub([a-zA-Z\d\s:],"",x)
        if s == reverse.lower():
            return True
        return False
