from typing import List


def combination_sum(candidates: List[int], target: int, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest_combination = None
    for candidate in candidates:
        reminder = target - candidate
        temp = combination_sum(candidates, reminder, memo)
        if temp is not None:
            temp_combination = temp + [candidate]
            if shortest_combination is None or len(shortest_combination) > len(temp_combination):
                shortest_combination = temp_combination
    memo[target] = shortest_combination
    return shortest_combination



print(combination_sum(candidates=[5,3,4,7], target=7))
print(combination_sum(candidates=[2,3,5], target=8))
print(combination_sum(candidates=[2,4], target=7))
print(combination_sum(candidates=[1,4,5], target=8))
print(combination_sum(candidates=[1,2,5,25], target=100))