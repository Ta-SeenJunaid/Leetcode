class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element, cur, win_count = max(arr), arr.pop(0), 0
        while True:
            opponent = arr.pop(0)
            if cur > opponent:
                win_count += 1
                arr.append(opponent)
            else:
                win_count = 1
                arr.append(cur)
                cur = opponent
            if win_count == k or cur == max_element:
                break
        return cur
    
