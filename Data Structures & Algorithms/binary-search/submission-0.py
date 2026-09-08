class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            i = 0
            while i <= mid:
                if nums[i] == target:
                    return i
                elif nums[i] != target and i == mid:
                    return -1
                i = i + 1
        elif nums[mid] < target:
            i = mid
            while i < len(nums):
                if nums[i] == target:
                    return i
                elif nums[i] != target and i == len(nums) - 1:
                    return -1
                i = i + 1
        else:
            return -1


        