class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        print(nums)
        indx = len(nums) - 2
        while indx >= 0 and nums[indx] >= nums[indx + 1]:
            indx -= 1
        
        if indx == -1:  return -1
        
        indx2 = len(nums) - 1
        while nums[indx2] <= nums[indx]:
            indx2 -= 1
        
        nums[indx], nums[indx2] = nums[indx2], nums[indx]
        nums[indx + 1:] = reversed(nums[indx + 1:])
        res = ""
        
        for num in nums:
            res += str(num)
        res = int(res)
        return res if res < 2 ** 31 else -1