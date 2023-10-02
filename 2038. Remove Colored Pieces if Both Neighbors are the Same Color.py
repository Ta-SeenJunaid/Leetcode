# https://www.youtube.com/watch?v=T54GScWobZ4 
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        for idx in range(1, len(colors) - 1):
            if colors[idx-1] == colors[idx] == colors[idx+1]:
                if colors[idx] == 'A':
                    alice += 1
                else:
                    bob += 1
        return alice > bob
      
