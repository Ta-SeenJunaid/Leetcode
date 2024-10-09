# https://www.youtube.com/watch?v=6kTZYvNNyps
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: # w1 = "fantastic" and # w2 = "fan"
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # True=visited, False=Current path & cycle
        topo_ans = []
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = False
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited[node] = True
            topo_ans.append(node)
            return True
        for node in adj:
            if not dfs(node):
                return ""
        return "".join(topo_ans[::-1])
        
