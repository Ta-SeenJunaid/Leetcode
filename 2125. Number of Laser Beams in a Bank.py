from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
            leaser_beams = 0
            previous_count = 0
            for row in bank:
                ones = row.count('1')
                if ones:
                    leaser_beams += ones*previous_count
                    previous_count = ones

            return leaser_beams


solution = Solution()
print(solution.numberOfBeams(bank = ["011001","000000","010100","001000"]))
print(solution.numberOfBeams(bank = ["000","111","000"]))
