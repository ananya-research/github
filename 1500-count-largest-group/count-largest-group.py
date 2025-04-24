class Solution:
    def countLargestGroup(self, n: int) -> int:

        ans=defaultdict(int)

        for i in range(1, 10):
            ans[i]=0

        print(ans)

        for i in range(1,n+1):

            j=i

            res=0

            while i:
                d=i%10
              
                res+=d
                
                i=i//10
               
            
            ans[res]+=1

        print(ans)

        res=0

        maxx=max(ans.values())
        c=0

        for v in ans.values():
            if v==maxx:
                c+=1
            

        return c
            


