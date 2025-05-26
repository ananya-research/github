class Solution:
    def countBits(self, n: int) -> List[int]:

        # def bits(k):
        #     ans=0
        #     if k==0:
        #         return 0
        #     while k!=0:
        #         ans+=1
        #         k=k&(k-1)
        #     return ans
        
        # final=[0]*(n+1)
        # for i in range(n+1):
        #     final[i]=bits(i)
        
        # return final

        dp=[0]*(n+1)
        offset=1

        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp
        
        