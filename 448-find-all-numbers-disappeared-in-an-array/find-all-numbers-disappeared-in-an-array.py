class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # missing=[]
        # for i in range(1,n+1):
        #     if i not in nums:
        #         missing.append(i)
        # return missing

        in_nums=set(nums)
        all_nums=set(range(1,len(nums)+1))
        return list(all_nums-in_nums)



        