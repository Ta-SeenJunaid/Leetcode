# https://www.youtube.com/watch?v=FVjKrhdMutc
# Max number of intersect is the answer

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        s, e = 0, 0
        res = 0
        intersect = 0
        while s < len(start):
            if start[s] <= end[e]:
                s += 1
                intersect += 1
            else:
                e += 1
                intersect -= 1
            res = max(res, intersect)
        return res
        
