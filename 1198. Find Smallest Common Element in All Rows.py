class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mat.sort()
        for i in mat[-1]:
            for j in range(len(mat)-1):
                if i not in mat[j]:
                    break
                if j ==  len(mat)-2:
                    return i
        return -1
