class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # m=max(candies)
        # ans=[]
        # n=len(candies)

        # for i in range(n):
        #     if candies[i]+extraCandies>=m:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans
        

        ans=[False]*len(candies)

        maxx=max(candies)

        for c in range(len(candies)):
            if candies[c]+extraCandies>=maxx:
                ans[c]=True
            
        return ans
