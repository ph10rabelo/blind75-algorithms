class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights.sort()
        tamanho = len(heights)
        res = heights[tamanho-1]*heights[tamanho-2]
        return res
