class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res =  []
        n = len(code)
        if k >= 0:
            for i in range(n):
                temp = 0
                for j in range(1, k+1):
                    temp += code[(i+j)%n]
                res.append(temp)
        else:
            for i in range(n):
                temp = 0
                for j in range(1, abs(k)+1):
                    temp += code[(i-j)%n]
                res.append(temp)
        return res
