class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s=s.replace("*","")
        # return(s)
        res=""
        stack=[]
        for i in s:
            if i=="*":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        for i in stack:
            res+=i
        return res