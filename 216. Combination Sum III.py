class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.recur(1, k, n, [])
        return self.ans

    def recur(self, idx, k, n, path):
        if n==0:
            if len(path) == k:
                self.ans.append(path)
            return
        if len(path) >= k:
            return
        if idx > 9:
            return
        self.recur(idx+1, k, n - idx, path + [idx])
        self.recur(idx+1, k, n, path)
