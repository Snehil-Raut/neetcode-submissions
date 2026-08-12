class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if ((bracket=='(') or (bracket=='[') or (bracket=='{')):
                stack.append(bracket)
            
            else:
                if len(stack) == 0:
                    return False
                else:
                    if ((stack[-1]=='(') and (bracket==')') or
                    (stack[-1]=='[') and (bracket==']') or
                    (stack[-1]=='{') and (bracket=='}')):
                        stack.pop()
                    else:
                        return False

        if len(stack)==0:
            return True
        else:
            return False

        