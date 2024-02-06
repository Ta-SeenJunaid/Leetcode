class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))].append(word)
        return dic.values()
        
