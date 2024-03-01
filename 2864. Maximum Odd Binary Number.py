# A binary string is odd if and only if the last bit (i.e. the one's place) equals 1

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count1 = s.count('1')
        return '1'*(count1-1) + '0'*(len(s)-count1) + '1'
