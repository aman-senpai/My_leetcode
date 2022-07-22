class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        running_sum = 0
        for n in nums:
            running_sum += n
            res.append(running_sum)
        return res