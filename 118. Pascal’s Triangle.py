class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        pre = [1, 1]
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            if i == 1:
                ans.append(pre)
                continue
            temp = []
            for j in range(len(pre)-1):
                temp.append(pre[j]+pre[j+1])
            temp = [1] + temp + [1]
            ans.append(temp)
            pre = temp
        return ans
