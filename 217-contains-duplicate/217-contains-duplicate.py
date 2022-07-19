class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for i in range(len(nums)):
            if nums[i] in _set: return True
            _set.add(nums[i])
        return False