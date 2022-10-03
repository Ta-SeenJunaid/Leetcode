from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort(reverse=True)
        # median = (arr[len(arr)//2] + arr[(len(arr)-1)//2]) // 2
        median = arr[(len(arr) - 1) // 2]
        l_p, r_p, result = 0, len(arr)-1, []
        while k > 0:
            if abs(arr[l_p] - median) >= abs(arr[r_p] - median):
                result.append(arr[l_p])
                l_p += 1
                k -= 1
                continue
            result.append(arr[r_p])
            r_p -= 1
            k -= 1
        return result

# class Solution:
#     def getStrongest(self, arr: List[int], k: int) -> List[int]:
#         m = sorted(arr)[(len(arr) - 1) // 2]
#         return sorted(arr, reverse=True, key = lambda x: (abs(x - m), x))[:k]


solution = Solution()
print(solution.getStrongest(arr = [1,2,3,4,5], k = 2))
print(solution.getStrongest(arr = [1,1,3,5,5], k = 2))
print(solution.getStrongest(arr = [6,7,11,7,6,8], k = 5))
print(solution.getStrongest(arr = [-7, 22, 17, 13], k = 2))