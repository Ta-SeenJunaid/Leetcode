# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# class Solution:
#     def search(self, reader: 'ArrayReader', target: int) -> int:
#         l, r = 0, 10000
#         while l <= r:
#             mid = (l+r)//2
#             val = reader.get(mid)
#             if val == target:
#                 return mid
#             elif val < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return -1

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/editorial        
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1
        
        while l <= r:
            pivot = (l+r) >> 1
            val = reader.get(pivot)
            if val == target:
                return pivot
            elif val < target:
                l = pivot + 1
            else:
                r = pivot - 1
        return -1
