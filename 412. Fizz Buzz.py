class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for n in range(1, n+1):
            d_by_3 = (n%3 == 0)
            d_by_5 = (n%5 == 0)
            if d_by_3 and d_by_5:
                ans.append("FizzBuzz")
            elif d_by_3:
                ans.append("Fizz")
            elif d_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(n))
        return ans
        
