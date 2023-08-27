class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high)//2
            if self.is_possible(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def is_possible(self, weights: List[int], days: int, ship_capacity) -> bool:
        re_days, cur_load = 1, 0
        for weight in weights:
            if cur_load + weight > ship_capacity:
                re_days += 1
                cur_load = weight
            else:
                cur_load += weight
        if re_days <= days:
            return True
        return False

