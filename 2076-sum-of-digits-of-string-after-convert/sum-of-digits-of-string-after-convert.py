class Solution:
    def getLucky(self, s: str, k: int) -> int:

        nums=""

        for l in s:
            val=ord(l)-96
            print(val)
            nums+=str(val)

        total=0

        while k>0:
            total=0
            for i in nums:
                total+=int(i)
            nums=str(total)
            k-=1

        return int(nums)

            

        