class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        start_color = image[sr][sc]
        while stack:
            r, c = stack.pop()
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] == color or image[r][c] != start_color:
                continue
            image[r][c] = color
            stack.append((r+1, c))
            stack.append((r-1, c))
            stack.append((r, c+1))
            stack.append((r, c-1))
        return image
