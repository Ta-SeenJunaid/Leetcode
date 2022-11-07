class Solution:
    def maximum69Number (self, num: int) -> int:
        # replace the 1st 6 to 9
        return int(str(num).replace('6', '9', 1))


solution = Solution()
print(solution.maximum69Number(num = 9669))
print(solution.maximum69Number(num = 9996))
print(solution.maximum69Number(num = 9999))