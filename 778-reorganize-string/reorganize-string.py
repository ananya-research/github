class Solution:
    def reorganizeString(self, s: str) -> str:

        n=len(s)

        c=Counter(s)

        max_heap=[]

        for char, count in c.items():
            max_heap.append((-count, char))

        heapq.heapify(max_heap)

        prev_count=0
        prev_char=""

        ans=[]

        while max_heap:
            count, char=heapq.heappop(max_heap)

            if prev_count<0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            if prev_char!=char:
                ans.append(char)

            prev_count=count+1
            prev_char=char
        
        return "".join(ans) if len(ans)==n else ""



















        # n=len(s)

        # char_count=Counter(s)

        # max_heap=[]

        # for char, count in char_count.items():
        #     max_heap.append((-count,char))

        # heapq.heapify(max_heap)

        # prev_count=0
        # prev_char=""

        # ans=[]

        # while max_heap:

        #     count, char=heapq.heappop(max_heap)

        #     if prev_count<0:
        #         heapq.heappush(max_heap, (prev_count, prev_char))

        #     if prev_char!=char:
        #         ans.append(char)
              
        #     prev_count=count+1
        #     prev_char=char

        # return "".join(ans) if n==len(ans) else ""

        





        