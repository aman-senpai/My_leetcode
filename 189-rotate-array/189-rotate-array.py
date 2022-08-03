class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        side = [0] * len(nums)
        
        for i, n in enumerate(nums):
            pos = (i + k) % len(nums)
            side[pos] = n
        for i, n in enumerate(side):
            nums[i] = n
    