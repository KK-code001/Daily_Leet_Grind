class Solution {
public:
    int mySqrt(int n) {
        int ans=0;
       for(long long int i=1;i*i<=n;i++){
        ans=i;
       } 
       return ans;
    }
};