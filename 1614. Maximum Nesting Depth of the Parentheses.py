class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            elif char == ')':
                depth -= 1
        return max_depth


solution = Solution()
print(solution.maxDepth(s = "(1+(2*3)+((8)/4))+1"))
print(solution.maxDepth(s = "(1)+((2))+(((3)))"))
