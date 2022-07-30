class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_value = {}
        cypher = 97
        cypher_text = []
        for char in key.replace(" ", ""):
            if char not in key_value:
                key_value[char] = chr(cypher)
                cypher += 1
                if cypher == 123:
                    cypher = 97

        for char in message:
            if char == " ":
                cypher_text.append(" ")
                continue
            cypher_text.append(key_value[char])

        return ''.join(cypher_text)


solution = Solution()
print(solution.decodeMessage(key = "the quick brown fox jumps over the lazy dog",
                             message = "vkbs bs t suepuv"))
print(solution.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo",
                             message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))