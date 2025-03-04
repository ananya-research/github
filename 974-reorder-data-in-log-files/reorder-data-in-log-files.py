class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        res=[]
        
        
        digit_log, letter_log=[], []
        
        def hasNum(inp):
            return any(char.isdigit() for char in inp)
        
        
        for i, log in enumerate(logs):
            vals=log.split(" ")
            
            if hasNum(vals[1:]):
                digit_log.append(log)
            else:
                letter_log.append([' '.join(vals[1:]), vals[0], i])

        print(letter_log)
        
                
        for log in sorted(letter_log):
            res.append(logs[log[2]])
            
        
        
        return res+digit_log
        