class Solution:
    def __init__(self):
        self.result = set()

    def numTilePossibilities(self, tiles: str) -> int:
        self.dfs_backtrack(tiles, "")
        return len(self.result)

    def dfs_backtrack(self, tiles: str, path):
        if not tiles:
            self.result.add(path)
            return
        for i in range(len(tiles)):
            if path and path not in self.result:
                self.result.add(path)
            self.dfs_backtrack(tiles[:i]+tiles[i+1:],path+tiles[i])


solution = Solution()
# print(solution.numTilePossibilities(tiles = "ABC"))
# print(solution.numTilePossibilities(tiles = "AAB"))
print(solution.numTilePossibilities(tiles = "AAABBC"))
# print(solution.numTilePossibilities(tiles = "V"))