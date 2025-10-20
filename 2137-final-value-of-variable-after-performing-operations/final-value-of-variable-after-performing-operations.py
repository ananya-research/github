class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        X=0

        for op in operations:

            if op=='--X' or op=='X--':
                X-=1
                continue
            else:
                X+=1
                continue
            
        return X
        