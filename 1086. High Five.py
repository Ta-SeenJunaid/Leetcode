class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse= True)
        temp, cnt = 0, 0
        cur_id = 0
        ans = []
        for i, s in items:
            if cur_id != i:
                cnt += 1
                temp += s
            if cnt == 5:
                ans.append([i, temp//5])
                temp = 0
                cnt = 0
                cur_id = i
        ans.sort()
        return ans
        
