class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # ans=""

        # for s in str1:
        #     if s in str2:
        #         if s not in ans:
        #             ans+=s
        
        # if ans in str1 or ans in str2:
        #     str1 = str1.replace(ans, "")
        #     str2 = str2.replace(ans, "")
        
        # if len(str1)==0 and len(str2)==0:
        #     return ans
        # else:
        #     return ""

        def gcd(a,b):

            while b:
                a,b=b,a%b
            return a
        
        if str1+str2!=str2+str1:
            return ""

        len1=len(str1)
        len2=len(str2)

        gcd_len=gcd(len1,len2)

        

        return str1[:gcd_len]

        
       
        