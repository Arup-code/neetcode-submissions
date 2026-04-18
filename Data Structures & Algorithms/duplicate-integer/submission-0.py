class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkset = set()
        for i in range(len(nums)):
            checkset.add(nums[i])
        return len(checkset) != len(nums)