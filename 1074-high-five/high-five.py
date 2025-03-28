class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_scores=defaultdict(list)
        for i, j in items:
            student_scores[i].append(j)
        result=[]
        for i,j in student_scores.items():
            top_five=sorted(j, reverse=True)[:5]
            avg=sum(top_five)//5
            result.append([i, avg])
        return sorted(result, key= lambda x:x)

        

            
        