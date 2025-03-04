class Solution:
    def trap(self, height: List[int]) -> int:

        # if not height: return 0

        # l, r = 0, len(height)-1
        # maxLeft, maxRight = height[l], height[r]
        # res=0

        # while l<r:

        #     if maxLeft<maxRight:
        #         l+=1
        #         ma xLeft = max(maxLeft, height[l])
        #         res+= maxLeft - height[l]
            
        #     else:
        #         r-=1
        #         maxRight = max(maxRight, height[r])
        #         res+= maxRight - height[r]
            
        # return res

        n=len(height)
        rwall=0
        lwall=0

        max_left=[0]*n
        max_right=[0]*n

        for i in range(n):
            j=-i-1
            max_left[i]=lwall
            max_right[j]=rwall
            lwall=max(lwall, height[i])
            rwall=max(rwall, height[j])

        summ=0
        for i in range(n):
            potential=min(max_left[i], max_right[i])
            summ+=max(0,potential-height[i])

        return summ
        