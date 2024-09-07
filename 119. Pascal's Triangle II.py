class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pre = [1, 1]
        for i in range(2, rowIndex+1):
            cur = []
            for j in range(len(pre)-1):
                cur.append(pre[j]+pre[j+1])
            cur = [1] + cur + [1]
            pre = cur
        return pre        
        
