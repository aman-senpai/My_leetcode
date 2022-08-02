class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            curSum = nums[l] + nums[r]
            if curSum == target:
                return [l + 1, r + 1]
            elif curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
        