# https://leetcode.com/problems/fruit-into-baskets/solutions/2960000/fruit-into-baskets/
# https://www.youtube.com/watch?v=Lav6St0W_pQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=10
# k = 2
from typing import List, Counter

# dict.get(key, default = None)
# key − This is the Key to be searched in the dictionary
# default − This is the Value to be returned in case key does not exist.

# person = {}
# # Using get() results in None
# print('Salary: ', person.get('salary'))
# # Using [] results in KeyError
# print(person['salary'])


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         basket = {}
#         left = 0
#         max_picked = 0
#         for right in range(len(fruits)):
#             basket[fruits[right]] = basket.get(fruits[right], 0) + 1
#
#             while len(basket) > 2:
#                 basket[fruits[left]] -= 1
#                 if basket[fruits[left]] == 0:
#                     del basket[fruits[left]]
#                 # don't understand
#                 left += 1
#             max_picked = max(max_picked, right - left + 1)
#         return max_picked


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l_p, max_picked = 0, 0
        for r_p in range(len(fruits)):
            basket[fruits[r_p]] = basket.get(fruits[r_p], 0) + 1
            k = 2
            while len(basket) > 2:
                basket[fruits[l_p]] -= 1
                if basket[fruits[l_p]] == 0:
                    del basket[fruits[l_p]]
                l_p += 1
            max_picked = max(max_picked, r_p - l_p +1)
        return max_picked


solution = Solution()
print(solution.totalFruit(fruits = [1,2,1]))
print(solution.totalFruit(fruits = [0,1,2,2]))
print(solution.totalFruit(fruits = [1,2,3,2,2]))
print(solution.totalFruit(fruits = [3,3,3,1,2,1,1,2,3,3,4]))
print(solution.totalFruit(fruits = [0,0,1,1]))
print(solution.totalFruit(fruits = [0,1,6,6,4,4,6]))




