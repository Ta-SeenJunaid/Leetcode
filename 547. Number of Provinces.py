class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = set()
        stack = []
        pro = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                stack.append(i)
                pro += 1
                while(stack):
                    c_node = stack.pop(0)
                    for nei in adj_list[c_node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
        return pro
