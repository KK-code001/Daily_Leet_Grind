class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        num=len(nums)/3
        for x in nums:
            d[x]=d.get(x,0)+1
        for i,j in d.items():
            if j>num:
                res.append(i)
        return res
        