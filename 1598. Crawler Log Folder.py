from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = []
        for i in range(0, len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i]=="../" and result:
                result.remove(result[-1])
            elif logs[i] == "../" and not result:
                continue
            else:
                result.append(logs[i])
        return len(result)


solution = Solution()
print(solution.minOperations(logs = ["d1/","d2/","../","d21/","./"]))
print(solution.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
print(solution.minOperations(logs = ["d1/","../","../","../"]))