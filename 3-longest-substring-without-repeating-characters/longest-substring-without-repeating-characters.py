class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # n=len(s)
        # longest=0
        # l=0
        # seen=set()
        
        # for r in range(n):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l+=1
        #     window_length=(r-l)+1
        #     longest=max(window_length, longest)
        #     seen.add(s[r])
        
        # return longest



        l=0
        r=0
        n=len(s)

        maxlen=0
        length=0
        seen=set()

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            length=r-l+1
            maxlen=max(maxlen, length)
            seen.add(s[r])
        
        return maxlen
            

        
        
        

      

        

























        # n=len(s)
        # m=set()

        # longest=0
        # l=0

        # for i in range(n):
        #     # if s[i] not in m:
        #     #     l+=1
        #     #     m.add(s[i])
        #     if s[i] in m:
                
        #         longest=max(l,longest)
        #         l=0
        #         m=set()
        #     elif s[i] not in m:
        #         l+=1
        #         m.add(s[i])

        #     longest=max(l,longest)
        
        # return longest

#         n=len(s)
#         l=0
#         sett=set()
#         longest=0

#         for r in range(n):
#             while s[r] in sett:
#                 sett.remove(s[l])
#                 l+=1
#             window_length=r-l+1
#             longest=max(longest,window_length)
#             sett.add(s[r])

#         return longest






















        