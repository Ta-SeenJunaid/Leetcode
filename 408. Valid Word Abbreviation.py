class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wp, ap = 0, 0
        wl, al = len(word), len(abbr)
        while wp < wl and ap < al:
            if word[wp] == abbr[ap]:
                wp += 1
                ap += 1
            elif abbr[ap] == "0":
                return False
            elif abbr[ap].isnumeric():
                k = ap
                while k < al and abbr[k].isnumeric():
                    k += 1
                wp += int(abbr[ap:k])
                ap = k
            else:
                return False 
        return wp == wl and ap == al
