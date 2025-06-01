class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        s=0
        self.left=left
        self.right=right

        for i in range(self.left, self.right+1, 1):
            s+=self.nums[i]
        
        return s
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)