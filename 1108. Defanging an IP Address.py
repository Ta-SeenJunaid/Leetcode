class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


solution = Solution()
print(solution.defangIPaddr(address = "1.1.1.1"))
print(solution.defangIPaddr(address = "255.100.50.0"))