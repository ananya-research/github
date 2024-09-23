class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        #for i, j in [event1, event2]:
            #print(i, j)
            #hhi, mmi = map(int, i.split(":"))
            #hhj, mmj = map(int, j.split(":"))
            #print(hhi, mmi)
            #print(hhj, mmj)
        return event1[0] <= event2[1] and event2[0] <= event1[1]
            



        