class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        n=len(s)
        m=len(t)

        if n!=m:
            return False

        map=dict()

        for i in range(n):
            if s[i] not in map:
                for value in map.values():
                    if value==t[i]:
                        return False
                map[s[i]]=t[i]
            else:
                if map[s[i]]!=t[i]:
                    return False
            
        return True


        # return False



        
        