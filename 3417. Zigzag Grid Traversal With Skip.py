class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        even = True
        ans = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                if even and j%2==0:
                    temp.append(grid[i][j])
                elif not even and j%2!=0:
                    temp.append(grid[i][j])
            if even:
                ans += temp
            else:
                ans += temp[::-1]
            even = not even
        return ans
