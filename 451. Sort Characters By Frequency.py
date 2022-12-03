from collections import Counter, OrderedDict


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_counter = Counter(s)
        freq_counter_sorted= OrderedDict(sorted(freq_counter.items(),reverse=True, key=lambda t: t[1]))
        result = ""
        for i in freq_counter_sorted:
            result += i*freq_counter_sorted[i]
        return result


solution = Solution()
print(solution.frequencySort(s = "tree"))
print(solution.frequencySort(s = "cccaaa"))
print(solution.frequencySort(s = "Aabb"))