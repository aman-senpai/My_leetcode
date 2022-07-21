class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        seenFrequency = {}
        output = []
        
        for num in nums1:
            if num in seenFrequency:
                seenFrequency[num] = seenFrequency[num] + 1
            else:
                seenFrequency[num] = 1
        
        for num in nums2:
            if num in seenFrequency and seenFrequency[num] > 0:
                output.append(num)
                seenFrequency[num] -= 1
        return output