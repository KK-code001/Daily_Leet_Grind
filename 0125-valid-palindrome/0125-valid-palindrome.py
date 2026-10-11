class Solution:
    def isPalindrome(self, s: str) -> bool:
        strn=s.strip().lower()
        strw=""
        for i in strn:
            if i.isalnum():
                strw+=i
        if strw==strw[::-1]:
            return True
        return False
        