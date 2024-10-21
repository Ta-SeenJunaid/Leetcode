class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        s = list(s)
        count = 0
        for i in range(n):
            if s[i] == 'a':
                count += 1
            else:
                break
        if count == n:
            return "a"*(n-1)+ "z"
        for i in range(count, n):
            if s[i] == 'a':
                break
            s[i] = chr(ord(s[i])-1)
        return "".join(s)
            
        
