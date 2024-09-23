class Solution:
    def compress(self, chars: List[str]) -> int:
        num_chars=len(chars)
        i=j=0

        if num_chars<=1:
            return 1

        while i< num_chars:
            count=1
            while i< num_chars-1 and chars[i]==chars[i+1]:
                count+=1
                i+=1

            chars[j]=chars[i]
            j+=1
            
            if count>1:
                for val in str(count):
                    chars[j]=val
                    j+=1
            i+=1

        return j







            
        