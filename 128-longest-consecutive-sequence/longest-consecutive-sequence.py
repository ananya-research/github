class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        n=len(nums)
        for num in s:
            if num -1 not in s:
                length=1
                #next_num=num+1
                while (num+length) in s:
                    length+=1
                    
                longest=max(longest,length)
        return longest

