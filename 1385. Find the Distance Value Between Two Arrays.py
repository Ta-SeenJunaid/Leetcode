from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        for i in arr1:
            temp=1
            for j in arr2:
                if abs(i-j) <= d:
                    temp =0
                    break
            count +=temp
        return count


solution = Solution()
print(solution.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print(solution.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
print(solution.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))
