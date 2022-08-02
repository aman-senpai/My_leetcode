class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for r in matrix:
            for e in r:
                arr.append(e)
        arr.sort()
        return arr[k - 1]