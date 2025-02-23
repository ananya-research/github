class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        m=s[:]
        n=len(s)
        print(m[0])
        s[:]=m[::-1]

        