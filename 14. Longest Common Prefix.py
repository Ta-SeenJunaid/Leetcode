class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while prefix != strs[i][0:len(prefix)]:
                if len(prefix) == 0:
                    return ""
                prefix = prefix[:len(prefix)-1]
        return prefix
        
