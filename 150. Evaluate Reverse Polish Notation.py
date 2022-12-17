import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        allowed_operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv}
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(int(allowed_operators[i](first_number,second_number)))
            else:
                stack.append(int(i))
        return stack[0]


solution = Solution()
print(solution.evalRPN(tokens = ["2","1","+","3","*"]))
print(solution.evalRPN(tokens = ["4","13","5","/","+"]))
print(solution.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))