class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False

                else:
                    k = stack.pop()
                    if k!=hashmap[c]:
                        return False
        return not stack            

        # for i in s:
        #     match i:
        #         case '(':
        #             stack.append('(')
        #         case '{':
        #             stack.append('{')
        #         case '[':
        #             stack.append('[')
        #         case ')':
        #             if(len(stack)>0 and stack[-1] == '('):
        #                 stack.pop()
        #             else:
        #                 return False
        #         case '}':
        #             if(len(stack)>0 and  stack[-1] == '{'):
        #                 stack.pop()
        #             else:
        #                 return False
        #         case ']':
        #             if(len(stack)>0 and stack[-1] == '['):
        #                 stack.pop()
        #             else:
        #                 return False
        # return len(stack) == 0
