class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for em_h in hours:
            if em_h >= target:
                ans += 1
        return ans 
        
