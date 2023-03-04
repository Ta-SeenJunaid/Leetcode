class Solution:
    def splitNum(self, num: int) -> int:
        temp = [x for x in str(num)]
        temp.sort()
        temp_even = ''.join(temp[0::2])
        temp_odd = ''.join(temp[1::2])
        return int(temp_even)+int(temp_odd)

solution = Solution()
print(solution.splitNum(num = 4325))
print(solution.splitNum(num = 687))