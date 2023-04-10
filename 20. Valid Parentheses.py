class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i in s[1:]:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                stack.append(i)
        return not stack


solution = Solution()
print(solution.isValid(s = "()"))
print(solution.isValid(s = "()[]{}"))
print(solution.isValid(s = "(]"))