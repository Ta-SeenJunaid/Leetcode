from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
            return True if n <= 0 else False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n <= 0:
                return True
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            if n <= 0:
                return True
        if len(flowerbed) >= 3:
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                if n <= 0:
                    return True
        return True if n<=0 else False


solution = Solution()
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))