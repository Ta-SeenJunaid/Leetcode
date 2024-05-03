# https://www.youtube.com/watch?v=EScgtaakx2U

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)

        for i in range(max(l1, l2)):
            n1 = 0 if i>=l1 else int(v1[i])
            n2 = 0 if i >=l2 else int(v2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0
