class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        
        for i in range(n + 1):
            res.append(self.ones(i))
        
        return res
        
    def ones(self, n):
        out = 0
        
        while n:
            n &= (n-1)
            out += 1
        return out