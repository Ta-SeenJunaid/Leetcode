from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in range(0, len(ops)):
            if ops[i] == "C":
                result.remove(result[-1])
            elif ops[i] == "D":
                result.append(2*result[-1])
            elif ops[i] == "+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(ops[i]))
        return sum(result)



solution=Solution()
print(solution.calPoints(ops = ["5","2","C","D","+"]))
print(solution.calPoints(ops = ["5","-2","4","C","D","9","+","+"]))
print(solution.calPoints(ops = ["1","C"]))