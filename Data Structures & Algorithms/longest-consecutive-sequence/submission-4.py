class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest = 0
        seen = {}
        for i in range(len(nums)):
            if nums[i]-1 not in num:
                length = 1
                current_num = num
                while nums[i] + length in num:
                    length = length + 1
                    seen[nums[i]+length] = length
                longest = max(longest,length)
        
        return longest
        