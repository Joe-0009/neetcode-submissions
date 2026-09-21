class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cmp =set(nums)

        return False if len(cmp) == len(nums) else True
