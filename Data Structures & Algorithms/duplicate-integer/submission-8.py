class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
      #   print(hashset) 
        return len(hashset) != len(nums)