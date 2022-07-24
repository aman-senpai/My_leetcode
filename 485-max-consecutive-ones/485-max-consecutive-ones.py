class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, MaxCount = 0, 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                MaxCount = max(count, MaxCount)
                count = 0
        return max(MaxCount, count)