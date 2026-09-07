class Solution:
    def isPalindrome(self, s: str) -> bool:
       f="".join(a.lower() for a in s if a.isalnum())
       return f == f[::-1]
        