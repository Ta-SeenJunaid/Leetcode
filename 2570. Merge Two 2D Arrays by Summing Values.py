class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1p, n2p, res = 0, 0, [] 
        for i in range(max(nums1[-1][0], nums2[-1][0])):
            temp = 0
            if n1p < len(nums1) and nums1[n1p][0] == (i+1):
                temp += nums1[n1p][1]
                n1p += 1
            if n2p < len(nums2) and nums2[n2p][0] == (i+1):
                temp += nums2[n2p][1]
                n2p += 1
            if temp:
                res.append([i+1,temp])
        return res
        
