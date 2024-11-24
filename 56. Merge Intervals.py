class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        i = 1
        while i < len(intervals):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1] = [ans[-1][0], intervals[i][1] if intervals[i][1] > ans[-1][1] else ans[-1][1]]
            else:
                ans.append(intervals[i])
            i += 1
        return ans
