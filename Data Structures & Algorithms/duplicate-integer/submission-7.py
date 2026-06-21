class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums != set(nums) :
           return False
        else :
           return True