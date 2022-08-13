class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circle = [x for x in nums]
        for n in nums:
            circle.append(n)
        
        res = []
        for i, n in enumerate(nums):
            for j in range(i, len(circle)):
                if circle[j] > n:
                    res.append(circle[j])
                    break
            else:
                res.append(-1)
        return res