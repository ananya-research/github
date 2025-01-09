class Solution:
    def alternateDigitSum(self, n: int) -> int:

        sum=0

        w=str(n)

        for i in range(len(w)):
            if i%2==0:
                sum+=int(w[i])
            else:
                sum-=int(w[i])

        return sum



        