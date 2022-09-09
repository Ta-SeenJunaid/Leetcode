from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        l_len = len(l)
        output = []
        for i in range(l_len):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort(reverse=True)
            if len(subarray) == 1:
                output.append(True)
                continue
            difference = subarray[0] - subarray[1]
            subarray_len = len(subarray)
            for j in range(subarray_len-1):
                if (subarray[j] - subarray[j+1]) != difference:
                    output.append(False)
                    break
                elif j+1 == subarray_len -1:
                    output.append(True)
        return output


solution = Solution()
print(solution.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
print(solution.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))