class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1
        return heapq.nlargest(k,seen,seen.get)
        



        