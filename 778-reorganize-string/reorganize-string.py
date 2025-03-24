class Solution:
    def reorganizeString(self, s: str) -> str:
        ans=[]

        n=len(s)

        char_count=Counter(s)

        print(char_count)
        
        max_heap=[]

        for char, count in char_count.items():
            max_heap.append((-count, char))

        heapq.heapify(max_heap)

        print(max_heap)

        prev_char=""
        prev_count=0

        while max_heap:
            count, char= heapq.heappop(max_heap)
            ans.append(char)

            if prev_count<0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            prev_count=count+1
            prev_char=char

        return "".join(ans) if n==len(ans) else ""










        

        