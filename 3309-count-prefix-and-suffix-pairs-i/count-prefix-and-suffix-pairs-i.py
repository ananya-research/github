class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        counter=0

        n=len(words)

        for i in range(n):
            for j in range(i+1,n):
                l=len(words[i])
                if words[i] in words[j][:l] and words[i] in words[j][-l:]:
                    counter+=1

        return counter 
        