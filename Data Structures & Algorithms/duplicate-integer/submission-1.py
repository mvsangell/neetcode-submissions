class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set(nums)
        if (len(lst) == len(nums)):
            return False
        return True
        