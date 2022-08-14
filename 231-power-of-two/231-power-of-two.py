class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
#         if n == 1:  return True
#         if n % 2 == 0:
#             i = 1
#             power = 2
            
#             while n > power:
#                 power = 2 ** i
#                 i += 1
#             if power == n:  return True
#         else:   return False