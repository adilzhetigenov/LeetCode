class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            match i:
                case '(':
                    stack.append('(')
                case '{':
                    stack.append('{')
                case '[':
                    stack.append('[')
                case ')':
                    if(len(stack)>0 and stack[-1] == '('):
                        stack.pop()
                    else:
                        return False
                case '}':
                    if(len(stack)>0 and  stack[-1] == '{'):
                        stack.pop()
                    else:
                        return False
                case ']':
                    if(len(stack)>0 and stack[-1] == '['):
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
