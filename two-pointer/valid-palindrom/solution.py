
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_limpa = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s_limpa == s_limpa[::-1]
