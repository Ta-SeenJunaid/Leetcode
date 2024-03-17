class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        itv_len = len(intervals)

        while i < itv_len and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < itv_len and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)

        while i < itv_len:
            ans.append(intervals[i])
            i += 1
        
        return ans

            
