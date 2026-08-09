class Solution:
    def bindec(self,a:str):
        decimal=int(a,2)
        return decimal
    def decbin(self, n: int):
        return bin(n)[2:]
    def addBinary(self, a: str, b: str) -> str:
        x=self.bindec(a)
        y=self.bindec(b)
        sum=x+y
        res=self.decbin(sum)
        return res

        