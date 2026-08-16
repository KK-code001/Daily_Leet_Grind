class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0

        freq = {0: 1}

        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in freq:
                count += freq[remainder]

            freq[remainder] = freq.get(remainder, 0) + 1

        return count