from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        import collections
        occurance = collections.Counter(arr)
        frequency_values = sorted(occurance.values(), reverse=True)
        half_arr_len = len(arr)//2
        sum_frequency_occurance = 0
        for index, value in enumerate(frequency_values):
            sum_frequency_occurance += value
            if sum_frequency_occurance >= half_arr_len:
                return index + 1
        return


solution = Solution()
print(solution.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
print(solution.minSetSize(arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))
print(solution.minSetSize(arr = [7,7,7,7,7,7]))

