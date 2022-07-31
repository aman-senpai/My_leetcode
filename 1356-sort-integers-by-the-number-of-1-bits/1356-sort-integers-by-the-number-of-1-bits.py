class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.hamming_weight(x), x))
    
    @staticmethod
    def hamming_weight(num: int) -> int:
        weight = 0

        while num:
            weight += 1
            num &= num - 1

        return weight