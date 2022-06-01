from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        for row in range(rows):
            image[row]=image[row][::-1]
            for col in range(cols):
                image[row][col] ^= 1
        return image


solution = Solution()
print(solution.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))
print(solution.flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
