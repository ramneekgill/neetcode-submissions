class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i])
            min_height = heights[i]
            for j in range(i+1, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, (j-i+1)*min_height)
        return max_area


        