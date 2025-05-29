from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # if k==len(nums):
        #     return nums
        

        # count=Counter(nums)
        # print(count)

        # return heapq.nlargest(k, count.keys(), key=count.get)


        n=len(nums)
        answer=[0]*(n+1)

        c=Counter(nums)

        for num, freq in c.items():
            if answer[freq]==0:
                answer[freq]=[num]
            else:
                answer[freq].append(num)
            
        ret=[]

        for i in range(n, -1, -1):
            if answer[i]!=0:
                ret.extend(answer[i])
            if len(ret)==k:
                break
            
        return ret

            

        