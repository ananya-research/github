class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        p=0
        q=0

        n=len(numbers)

        for i in range(n):
            diff=target-numbers[i]
            if diff in numbers:
                ind=numbers.index(diff)
                if i<ind:
                    return [i+1, ind+1]
                elif i>ind:
                    return [ind+1,i+1]
                else:
                    continue
                




        