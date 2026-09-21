class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1

        for num in nums:
            prefix.append(product)
            product *= num

        suffix = []
        product = 1

        for num in reversed(nums):
            suffix.append(product)
            product *= num
        suffix.reverse()
        return [suffix[i] * prefix[i] for i in range(len(nums))]