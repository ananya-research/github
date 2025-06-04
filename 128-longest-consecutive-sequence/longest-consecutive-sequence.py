class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n=len(nums)

        numSet=set(nums)
        longest=0

        for num in numSet:
            if num-1 not in numSet:
                length=1

                while num+length in numSet:
                    length+=1
                
                longest=max(longest,length)
            
        return longest
























        # s=set(nums)
        # longest=0
        # n=len(nums)
        # for num in s:
        #     if num -1 not in s:
        #         length=1
        #         next_num=num+1
        #         while next_num in s:
        #             length+=1
        #             next_num+=1
        #         longest=max(longest,length)
        # return longest

