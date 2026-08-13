class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l,count=1,1
        nums=sorted(set(nums))
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            l=max(count,l)

        return l
        