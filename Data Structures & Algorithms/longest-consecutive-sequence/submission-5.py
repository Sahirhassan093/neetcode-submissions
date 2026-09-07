class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in num:
                length = 1
                while nums[i] + length in num:
                    length = length + 1
                longest = max(longest,length)
        
        return longest
        