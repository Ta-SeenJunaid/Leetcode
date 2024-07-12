# https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/5463276/beats-100-easy-to-understand-c-java-python-js-greedy-and-stack-solution/?envType=daily-question&envId=2024-07-12
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_p = 0
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair=="ab" else "ab"

        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) // 2
        max_p += removed_pairs_count*max(x,y)
        string_after_second_pass = self.remove_substring(string_after_first_pass, low_priority_pair)
        removed_pairs_count = (len(string_after_first_pass) - len(string_after_second_pass)) // 2 
        max_p += removed_pairs_count*min(x,y)
        return max_p

    def remove_substring(self, s, target_pair):
        char_stack = []
        for cur_char in s:
            if cur_char == target_pair[1] and char_stack and char_stack[-1] == target_pair[0]:
                char_stack.pop()
            else:
                char_stack.append(cur_char)
        return "".join(char_stack)
