class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == set(nums) :
           return false
        else :
           return true