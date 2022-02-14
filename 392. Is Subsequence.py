
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        count = 0
        for char in range(len(t)):
            if s[count] == t[char]:
                count += 1
            if len(s) == count:
                return True

        return False


solution = Solution()
print(solution.isSubsequence(s = "abc", t = "ahbgdc"))
print(solution.isSubsequence(s = "axc", t = "ahbgdc"))
print(solution.isSubsequence(s = "b", t = "abc"))
print(solution.isSubsequence(s = "", t = "abc"))