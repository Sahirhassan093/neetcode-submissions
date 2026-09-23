class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int mid = r - l / 2;
        for(int i =l;i<=r;i++){
            if(nums[i] == target){
                return i;
            }
        }
        return -1;
    }
}
