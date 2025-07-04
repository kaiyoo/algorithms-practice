# You are given an image represented by an m x n grid of integers image, 
# where image[i][j] represents the pixel value of the image. 
# You are also given three integers sr, sc, and color. 
# Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:
# 1. Begin with the starting pixel and change its color to color.
# 2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# 3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# 4. The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
 
# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]

# Explanation:
# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n

########
# approach: 
# 1) DFS: dfs(): if out-of-condition: return; assign & call dfs (4 times). Update image in global scope
# 2) BFS: while queue: queue.popleft(); for next search: assign & queue.append(next) 
# DFS should have stop-break condition
########

from collections import deque
class Solution(object):
    def floodFill_DFS(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        original_color = image[sr][sc]
        if original_color == color:
            return image  # 색이 같으면 무한루프 방지
        
        def dfs(r, c):
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != original_color):
                return
    
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)        

        dfs(sr, sc)    
            
        return image
    

    def floodFill_BFS(self, image, sr, sc, color):

        original_color = image[sr][sc]
        if original_color == color:
            return image

        queue = deque()
        queue.append((sr, sc))

        while queue:
            r, c = queue.popleft()
            for r_adjustment, c_adjustment in [(-1, 0), (1, 0),
                                               (0, -1), (0, 1)]:
                next_r, next_c = r + r_adjustment, c + c_adjustment

                if (0 <= next_r < len(image) and 
                    0 <= next_c < len(image[0]) and 
                    image[next_r][next_c]==original_color):

                    image[next_r][next_c] = color
                    queue.append((next_r, next_c))
            
        return image
        
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

# image = [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# color = 0
# Output: [[0,0,0],[0,0,0]]

# Solution 1 - DFS
# answer = Solution().floodFill_DFS(image, sr, sc, color)
# print(answer)

# Solution 2 - BFS
answer = Solution().floodFill_BFS(image, sr, sc, color)
print(answer)