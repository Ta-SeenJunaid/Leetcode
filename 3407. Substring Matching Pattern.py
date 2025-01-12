class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pattern = p.replace('*','.*')
        return bool(re.search(pattern, s))
