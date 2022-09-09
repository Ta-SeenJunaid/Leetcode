from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_len = len(s)
        hash_map = {}
        ans = []
        for i in range(s_len):
            hash_map[s[i]] = i
        left_pointer, right_pointer = 0, hash_map[s[0]]
        for i in range(s_len):
            if i<= right_pointer:
                right_pointer = max(right_pointer, hash_map[s[i]])
            else:
                ans.append(right_pointer-left_pointer+1)
                left_pointer = i
                right_pointer = hash_map[s[i]]
        ans.append(right_pointer - left_pointer + 1)
        return ans


solution = Solution()
print(solution.partitionLabels(s = "ababcbacadefegdehijhklij"))
print(solution.partitionLabels(s = "eccbbbbdec"))
