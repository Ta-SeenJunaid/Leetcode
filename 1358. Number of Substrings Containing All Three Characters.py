
# Time limit exceeded
# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         left_pointer = right_pointer = result = 0
#         s_len = len(s)
#         while left_pointer <= right_pointer and left_pointer < s_len:
#             if 'a' in s[left_pointer:right_pointer] and 'b' in s[left_pointer:right_pointer] \
#                     and 'c' in s[left_pointer:right_pointer]:
#                 result += 1
#
#             if right_pointer < s_len:
#                 right_pointer += 1
#             else:
#                 left_pointer += 1
#                 right_pointer = left_pointer
#         return result

# https://www.youtube.com/watch?v=VNL2VhDxj7U
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        index_a = index_b = index_c = -1
        count = 0
        for i, x in enumerate(s):
            if x == 'a':
                index_a = i
            elif x == 'b':
                index_b = i
            else:
                index_c = i
            count += min(index_a, index_b, index_c) + 1
        return count


solution = Solution()
print(solution.numberOfSubstrings(s = "abcabc"))
print(solution.numberOfSubstrings(s = "aaacb"))
print(solution.numberOfSubstrings(s = "abc"))
