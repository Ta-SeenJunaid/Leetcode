from typing import List


def combination_sum(candidates: List[int], target: int, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in candidates:
        reminder = target - i
        if combination_sum(candidates, reminder):
            memo[target] = True
            return True

    memo[target] = False
    # print(memo)
    return False


# print(combination_sum([2,3], 7))
# print(combination_sum([5, 3, 4, 7], 7))
# print(combination_sum([2,4], 7))
# print(combination_sum([2,3, 5], 8))
print(combination_sum([7, 14], 300))

