class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low, high = min(bloomDay), max(bloomDay)
        while low <= high:
            mid = (low + high)//2
            if self.is_possible(bloomDay, m, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def is_possible(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        count, possible = 0, 0
        for i in bloomDay:
            if day >= i:
                count += 1
            else:
                possible += count//k
                count = 0
            if possible >= m:
                return True
        possible += count//k
        if  possible >= m:
            return True
        else:
            return False
