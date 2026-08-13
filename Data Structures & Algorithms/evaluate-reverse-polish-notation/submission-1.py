import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for op in tokens:
            if op.lstrip("-").isdigit():
                num_stack.append(int(op))

            else:
                if (op=='+' or op=='-' or op=='*' or op=='/') and (op in ops):
                    fele = num_stack.pop()
                    secele = num_stack.pop()

                    res = ops[op](secele,fele)
                    num_stack.append(int(res))
        return num_stack[0]