class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i+2>j:
                return 0
            if i+2==j:
                return (values[i]*values[i+1]*values[j])

            fin_val=float('inf')
            
            for k in range(i+1,j):
                val=values[i]*values[k]*values[j] + dp(i,k)+dp(k,j)
                fin_val=min(val,fin_val)
            return fin_val
        
        return dp(0, len(values)-1)

        