class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            temp = []
            for c in combs:
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
            combs = temp
        return combs
#         res = []
        
#         def backtrack(start, comb: list):
#             if len(comb) == k:
#                 res.append(comb.copy())
#                 return
            
#             for i in range(start, n + 1):
#                 comb.append(i)
#                 backtrack(i + 1, comb)
#                 comb.pop()
#         backtrack(1, [])
#         return res