from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        count = 0
        len_arr = len(arr)
        for i in range(len_arr):
            if i < k - 1:
                count += arr[i]
            elif i == k -1:
                count += arr[i]
                if count >= threshold * k:
                    result += 1
            else:
                count += arr[i]
                count -= arr[i-k]
                if count >= threshold * k:
                    result += 1
        return result


solution = Solution()
print(solution.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(solution.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))

