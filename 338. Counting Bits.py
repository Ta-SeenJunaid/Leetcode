class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n+1):
            ans.append(bin(i).count("1"))

        return ans


solution = Solution()
print(solution.countBits(2))
print(solution.countBits(5))