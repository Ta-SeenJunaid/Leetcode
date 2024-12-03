class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digit = {"0": "0", "1":"1", "6": "9", "8": "8", "9":"6"}
        lp, rp = 0, len(num) - 1
        while lp <= rp:
            if num[lp] not in rotated_digit or rotated_digit[num[lp]] != num[rp]:
                return False
            lp += 1
            rp -= 1
        return True
