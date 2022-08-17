from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.",
                      "....","..",".---","-.-",".-..","--","-.","---",".--.",
                      "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformed_list = []
        for word in words:
            temp = ""
            for character in word:
                temp += morse_code[ord(character)-97]
            transformed_list.append(temp)
        from collections import Counter
        return len(Counter(transformed_list))


solution = Solution()
print(solution.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
print(solution.uniqueMorseRepresentations(words = ["a"]))
