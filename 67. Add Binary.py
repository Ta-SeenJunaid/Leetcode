class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2)).removeprefix('0b')


solution = Solution()
print(solution.addBinary(a = "11", b = "1"))
print(solution.addBinary(a = "1010", b = "1011"))