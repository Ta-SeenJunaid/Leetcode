from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dict = defaultdict(int)
        for num in nums:
            cnt_dict[num] += 1
        cnt_dict = sorted(cnt_dict.items(), key = lambda item: item[1], reverse=True)
        return [i for i, _ in cnt_dict][:k]
        
