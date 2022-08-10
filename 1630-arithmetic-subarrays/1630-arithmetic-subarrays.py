class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            #print(nums[l[i]:r[i]+1])
            a = nums[l[i]:r[i]+1]
            a.sort()
            x = self.check(a)
            #print(x)
            res.append(x)
        return res
        
    def check(self,arr):
        if len(arr) == 2:
            return True
        for i in range(1,len(arr)-1):
            if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
                return False
        return True