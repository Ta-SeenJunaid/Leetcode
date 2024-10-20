class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        cur_min = float("inf")
        ans = []
        n = len(arr)
        arr.sort()
        for i in range(n-1):
            dif = arr[i+1] - arr[i]
            if dif < cur_min:
                ans = [[arr[i], arr[i+1]]]
                cur_min = dif
            elif dif == cur_min:
                ans.append([arr[i], arr[i+1]])
        return ans
        
