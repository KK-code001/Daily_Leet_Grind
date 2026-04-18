class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            j=0
            while(j<len(haystack)):
                if haystack[j:j+len(needle)]==needle:
                    return j
                j+=1
        else:
            return -1