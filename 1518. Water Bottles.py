class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_drink = 0
        while numBottles >= numExchange:
            n = numBottles // numExchange
            max_drink += numExchange * n
            numBottles -= n*numExchange
            numBottles += n
        return max_drink + numBottles
   
