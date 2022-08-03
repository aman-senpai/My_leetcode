class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            left, right = nums[l] ** 2, nums[r] ** 2
            if left > right:
                res.append(left)
                l += 1
            else:
                res.append(right)
                r -= 1
        return res[::-1]