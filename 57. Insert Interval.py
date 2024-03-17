class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        if intervals == ans:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                j = i
                while j < len(intervals) and newInterval[1] >= intervals[j][0]:
                    j += 1
                ans.append([intervals[i][0] if intervals[i][0] < newInterval[0] else newInterval[0], 
                intervals[j-1][1] if intervals[j-1][1] > newInterval[1] else newInterval[1]])
                while j < len(intervals):
                    ans.append(intervals[j])
                    j += 1
                break
            ans.append(intervals[i])
            if i == len(intervals) - 1:
                ans.append(newInterval)
        return ans
            
