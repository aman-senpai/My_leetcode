class NumArray:

    def __init__(self, nums: List[int]):
        
        self.size = len(nums)  
        if self.size:
            self.prefix_sum = [0] * (self.size)
            self.prefix_sum[0] = nums[0]
            for k in range(1,self.size):
                self.prefix_sum[k] = self.prefix_sum[k-1] + nums[k]
        

    def sumRange(self, i: int, j: int) -> int:
        
        if self.size == 0 or i < 0 or i > j or j >= self.size:
            return 0

        if i == 0:
            return self.prefix_sum[j]
        else:
            return self.prefix_sum[j]-self.prefix_sum[i-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)