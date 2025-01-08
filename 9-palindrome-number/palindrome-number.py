class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        if m==(m[::-1]):
            print(m[::-1])
            return True
        return False
    
        