class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count, sp, tp = 0, 0, 0
        for idx in range(len(s)):
            if tp < len(t) and s[idx] == t[tp]:
                tp += 1
        count += len(t) - tp
        return count
        
