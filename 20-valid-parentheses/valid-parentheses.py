class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap={')':'(', '}':'{', ']':'['}

        # stack=[]

        # for c in s:
        #     if c not in hashmap:
        #         stack.append(c)
        #     else:
        #         if not stack:
        #             return False
        #         if stack:
        #             popped=stack.pop()
        #             if popped!=hashmap[c]:
        #                 return False
        # return not stack

        map={')':'(', ']':'[', '}':'{'}
        stack=[]

        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    ele=stack.pop()
                    if ele!=map[c]:
                        return False
                    
        if stack:
            return False
        return True
