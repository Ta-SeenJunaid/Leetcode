class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        if a > b:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, a
        left, t_len = (a+b+1)//2, a+b
        while True:
            m1 = (low+high)//2
            m2 = left - m1
            l1 = nums1[m1-1] if m1-1 >= 0 else float('-inf')
            l2 = nums2[m2-1] if m2-1 >= 0 else float('-inf')
            r1 = nums1[m1] if m1 < a else float('inf')
            r2 = nums2[m2] if m2 < b else float('inf')
            if l1 <= r2 and l2 <= r1:
                if t_len % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = m1 - 1
            else:
                low = m1 + 1

