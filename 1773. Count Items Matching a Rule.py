from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        return sum(item[index] == ruleValue for item in items)


solution = Solution()
print(solution.countMatches(items = [["phone","blue","pixel"],
                                     ["computer","silver","lenovo"],
                                     ["phone","gold","iphone"]],
                            ruleKey = "color", ruleValue = "silver"))
print(solution.countMatches(items = [["phone","blue","pixel"],
                                     ["computer","silver","phone"],
                                     ["phone","gold","iphone"]],
                            ruleKey = "type", ruleValue = "phone"))
