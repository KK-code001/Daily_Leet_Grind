class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # if len(stones)==1:
        #     return False
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        c0, c1, c2 = cnt

        if min(c1, c2) == 0:
            return max(c1, c2) > 2 and c0 % 2 == 1

        return abs(c1 - c2) > 2 or c0 % 2 == 0