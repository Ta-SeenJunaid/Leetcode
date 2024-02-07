class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        for char, count in  Counter(s).most_common():
            ans += char*count
        return ans
        
