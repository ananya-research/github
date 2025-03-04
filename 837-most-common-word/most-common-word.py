from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        para="".join([c.lower() if c.isalnum() else " " for c in paragraph])
        print(para)

        words=para.split()
        print(words)

        c=defaultdict(int)

        for w in words:
            if w not in banned:
                c[w]+=1

        return max(c, key=c.get)
        


        
        