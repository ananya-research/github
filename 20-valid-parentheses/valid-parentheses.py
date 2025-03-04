class Solution:
    def isValid(self, s: str) -> bool:
        # stack=[]
        # mapping={')':'(', ']':'[', '}':'{'}

        # for char in s:
        #     if char in mapping:
        #         top_ele=stack.pop() if stack else '#'
        #         if mapping[char]!=top_ele:
        #             return False
        #     else:
        #         stack.append(char)


        # return not stack

        hashmap={')':'(', '}':'{', ']':'['}

        stack=[]

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack:
                    popped=stack.pop()
                    if popped!=hashmap[c]:
                        return False
        return not stack

        