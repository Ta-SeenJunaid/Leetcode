from typing import List


def combination_sum(candidates: List[int], target: int, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for i in candidates:
        reminder = target - i
        temp = combination_sum(candidates, reminder, memo)
        if temp is not None:
            memo[target] = temp + [i]
            return memo[target]

    memo[target] = None
    return None


# print(combination_sum([2,3], 7))
# print(combination_sum([5, 3, 4, 7], 7))
# print(combination_sum([2,4], 7))
# print(combination_sum([2,3, 5], 8))
print(combination_sum([7, 14], 300))

