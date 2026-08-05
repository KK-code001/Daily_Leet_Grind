class Solution:
    def gcod(self,a,b):
        if b==0:
            return a
        return self.gcod(b,a%b)
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum1,sum2=0,0
        for i in range(1,n+1):
            sum1 += 2 * i - 1   
            sum2 += 2 * i 
        return self.gcod(sum1,sum2)