# https://leetcode.com/problems/zigzag-conversion/solutions/2868537/zigzag-conversion/
from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        s_len = len(s)
        num_section = ceil(s_len/(2*numRows-2))
        num_colms = num_section*(numRows-1)
        matrix = [[""]*num_colms for _ in range(numRows)]
        cur_row, cur_col, cur_count = 0, 0, 0
        while cur_count < s_len:
            while cur_row<numRows and cur_count < s_len:
                matrix[cur_row][cur_col] = s[cur_count]
                cur_row += 1
                cur_count += 1
            cur_row -= 2
            cur_col += 1
            while cur_row > 0 and cur_count < s_len:
                matrix[cur_row][cur_col] = s[cur_count]
                cur_row -= 1
                cur_col += 1
                cur_count +=1
        result = ""
        for i in matrix:
            result += "".join(i)
        return result

solution = Solution()
print(solution.convert(s = "PAYPALISHIRING", numRows = 3))
print(solution.convert(s = "PAYPALISHIRING", numRows = 4))
print(solution.convert(s = "A", numRows = 1))