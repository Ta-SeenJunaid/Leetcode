from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        if target<letters[left] or target >= letters[right]:
            return letters[left]
        while left <= right:
            mid =(left+right)//2
            if letters[mid]>target:
                right=mid-1
            else:
                left=mid+1
        #left, right and mid got the same value and then left increase by 1
        return letters[left]


solution = Solution()
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(solution.nextGreatestLetter(letters = ["c","f","j"], target = "d"))
print(solution.nextGreatestLetter(letters = ['a', 'b'], target = "z"))


