class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        if n == 2:
            return 1

        first, second, third = 0, 1, 1

        for _ in range(3, n+1):
            first, second, third = second, third, first+second+third

        return third