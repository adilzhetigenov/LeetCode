class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+':lambda a,b:a+b,
                    '*':lambda a,b:a*b, 
                    '-':lambda a,b:a-b,
                    '/':lambda a,b:int(a/b)}
        for t in tokens:
            if t in operators:
                b,a = stack.pop(),stack.pop()
                stack.append(operators[t](a,b))
            else:
                stack.append(int(t))
            
        # for t in tokens:
        #     match t:
        #         case '+':
        #             b,a = stack.pop(),stack.pop()
        #             stack.append(a + b)
        #         case '-':
        #             b,a = stack.pop(),stack.pop()
        #             stack.append(a - b)
        #         case '*':
        #             b,a = stack.pop(),stack.pop()
        #             stack.append(a * b)
        #         case '/':
        #             b,a = stack.pop(),stack.pop()
        #             stack.append(int(a / b))
        #         case _:
        #             stack.append(int(t))

        #     # if t in {'+', '-', '*', '/'}:
        #     #     b = stack.pop()
        #     #     a = stack.pop()
        #     #     if t == '+':
        #     #         stack.append(a + b)
        #     #     elif t == '-':
        #     #         stack.append(a - b)
        #     #     elif t == '*':
        #     #         stack.append(a * b)
        #     #     elif t == '/':
        #     #         stack.append(int(a / b))
        #     # else:
        #     #     stack.append(int(t))
        return stack[0]