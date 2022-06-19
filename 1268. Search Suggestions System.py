from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for c in range(1, len(searchWord)+1):
            temp = []
            count = 0
            for product in products:
                if product[0:c] == searchWord[0:c]:
                    temp.append(product)
                    count += 1
                if count == 3:
                    break
            ans.append(temp)

        return ans


solution = Solution()
print(solution.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"],
                                 searchWord = "mouse"))
print(solution.suggestedProducts(products = ["havana"], searchWord = "havana"))
print(solution.suggestedProducts(products = ["bags","baggage","banner","box","cloths"],
                                 searchWord = "bags"))
