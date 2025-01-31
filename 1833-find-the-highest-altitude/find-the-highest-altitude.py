class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        

        #ans[0]=0

        n=len(gain)

        ans=[0]*(n+1)

        for i in range(n):
            ans[i+1]=gain[i]+ans[i]
        
        return max(ans)
        
        