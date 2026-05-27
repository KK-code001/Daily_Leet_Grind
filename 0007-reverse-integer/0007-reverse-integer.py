class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            st=str(x)
            num=st[::-1]
            if -1*int(num[:len(num)-1]) not in range(-2**31, 2**31 - 1):
                return 0
            return -1*int(num[:len(num)-1])
        st=str(x)
        num=st[::-1]
        if int(num) not in range(-2**31, 2**31 - 1):
                return 0
        return int(num)
