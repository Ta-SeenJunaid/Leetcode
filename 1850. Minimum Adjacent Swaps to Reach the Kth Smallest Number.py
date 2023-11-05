# https://www.youtube.com/watch?v=XmkAQTokN4M

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num = list(num)
        orig = num.copy()

        for _ in range(k):
            num = self.next_permutation(num)
        swap = 0
        print(num)
        for i in range(len(num)):
            ii = i
            while orig[i] != num[i]:
                swap += 1
                ii += 1
                num[i], num[ii] = num[ii], num[i]
        return swap

    def next_permutation(self, nums: List[int]):
        len_nums = len(nums)
        if len_nums <= 2:
            return nums[::-1]
        fi_p, se_p = len(nums) - 2, len(nums) - 1
        while fi_p >= 0:
            if nums[fi_p] >= nums[fi_p+1]:
                fi_p -= 1
            else:
                while se_p > fi_p:
                    if nums[se_p] <= nums[fi_p]:
                        se_p -= 1
                    else:
                        nums[fi_p], nums[se_p] =  nums[se_p], nums[fi_p]
                        nums[fi_p+1:len_nums] = reversed(nums[fi_p+1:len_nums])
                        return nums
        return nums[::-1]
        
