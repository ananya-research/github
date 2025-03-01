class Solution:
    def maxArea(self, height: List[int]) -> int:

        n=len(height)

        l=0
        r=n-1

        area=0
        ar=0

        while l<r:
            ar=abs((r-l)*(min(height[r],height[l])))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            area=max(ar,area)

        return area


        