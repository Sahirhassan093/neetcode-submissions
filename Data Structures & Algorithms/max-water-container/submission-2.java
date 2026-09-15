class Solution {
    public int maxArea(int[] heights) {
        int max_A = 0;
        int l = 0;
        int r = heights.length - 1;
        while (l < r){
            int wid = r - l;
            int h = Math.min(heights[l],heights[r]);
            int area = wid * h;
            max_A = Math.max(max_A,area);
            if (heights[l] < heights[r]){
               l = l + 1;
            }
            else{
                r = r - 1;
            }
        }
        return max_A;
    }
}
