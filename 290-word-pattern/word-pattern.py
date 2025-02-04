class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words=[]
        for i in s.split(" "):
            words.append(i)

        print(words)

        n=len(words)
        m=len(pattern)

        if n!=m:
            return False

        map=dict()
        

        for i in range(m):
            
            if pattern[i] in map:
                if map[pattern[i]]!=words[i]:
                    return False

            if words[i] in map.values():
                if pattern[i] not in map.keys():
                    return False 

            
            else:
                map[pattern[i]]=words[i]

        return True

        
