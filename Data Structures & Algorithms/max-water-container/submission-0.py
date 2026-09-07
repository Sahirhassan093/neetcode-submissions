class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_A = 0
        while l < r:
            A = (r - l)*(min(heights[l],heights[r]))
            max_A = max(A,max_A)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return max_A
        