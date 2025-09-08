class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n=len(words)
        length=0
        line=[]
        result=[]
        i=0

        while i<n:
            if len(line)+length+len(words[i])>maxWidth:
                extra_spaces=maxWidth-length
                spaces=extra_spaces//max(1, len(line)-1)
                remainder=extra_spaces%max(1,len(line)-1)
                for j in range( max (1, len(line)-1 ) ):
                    line[j]+=" "*spaces
                    if remainder:
                        line[j]+=" "
                        remainder-=1
                result.append("".join(line))
                line, length=[], 0
            line.append(words[i])
            length+=len(words[i])
            i+=1

        last_line=" ".join(line)
        trailing_spaces=maxWidth-len(last_line)
        last_line+=" "*trailing_spaces
        result.append(last_line)
        return result

                    
        