from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        result = []
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for s in path[1:]:
                s = s.split(".txt")
                name = s[0]
                content = s[1]
                result_dict[content].append((folder, name))

        for k,v in result_dict.items():
            if len(v) > 1:
                tmp = []
                for path, name in v:
                    tmp.append(path+'/'+name+'.txt')
                result.append(tmp)
        return result


solution = Solution()
print(solution.findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(solution.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))
