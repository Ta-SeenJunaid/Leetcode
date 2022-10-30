class Solution:
    def longestDecomposition(self, text: str) -> int:
        left_p, right_p = 0, len(text)
        count, temp = 0, 0
        while left_p < right_p:
            temp += 1
            if text[left_p:left_p+temp] == text[right_p - temp:right_p]:
                if left_p+temp == right_p:
                    count += 1
                else:
                    count += 2
                left_p += temp
                right_p -= temp
                temp = 0
        return count


solution = Solution()
print(solution.longestDecomposition(text = "ghiabcdefhelloadamhelloabcdefghi"))
print(solution.longestDecomposition(text = "merchant"))
print(solution.longestDecomposition(text = "antaprezatepzapreanta"))
print(solution.longestDecomposition(text= "elvtoelvto"))