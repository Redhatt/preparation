from debug import *
S = lambda :input().strip()
L = lambda :list(map(int, input().split()))
I = lambda :int(input().strip())
T = lambda :map(int, input().split())


#==============================================
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:      
        stack = []
        for i,j in zip(s,locked):
            if i == ')' and stack and stack[-1][0] == '(': stack.pop()
            else: stack.append((i,j))

        if len(stack)&1: return False

        def validate(a, op):
            x = 0
            for i,j in a:
                if i == op:
                    print(i,j)
                    x += (1 if j == '0' else -1)  
                    print(x)
                if x < 0: return False
            return True

        print(validate(stack, ')') , validate(stack[::-1], '('))
        return validate(stack, ')') and validate(stack[::-1], '(')

#==============================================
solution = Solution()

a = S()
b = S()

result = solution.canBeValid(a,b)
debug(result=result)