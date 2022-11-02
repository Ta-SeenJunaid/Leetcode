# https://www.youtube.com/watch?v=wIsJ6G5qXkI
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        queue = [(start, 0)]
        visited = {start}
        while queue:
            # have to pass parameter 0 at lest.pop
            gene, level = queue.pop(0)
            if gene == end:
                return level
            gene_len = len(gene)
            for i in range(gene_len):
                for j in 'ACGT':
                    new_gene = gene[:i] + j + gene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        queue.append((new_gene, level+1))
                        visited.add(new_gene)
        return -1


solution = Solution()
print(solution.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(solution.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(solution.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))
print(solution.minMutation(start = "AAAACCCC", end = "CCCCCCCC", bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
