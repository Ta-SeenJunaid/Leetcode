class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        temp = []
        for g in grid:
            for e in g:
                temp.append(e)
        temp.sort()
        return temp[len(temp)//2]
