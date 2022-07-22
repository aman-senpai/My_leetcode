class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth_so_far = 0
        
        def sum_help(l1):
            _sum = 0
            for l in l1:
                _sum += l
            return _sum
        
        for account in accounts:
            
            curr_customer_wealth = sum_help(account)
            
            max_wealth_so_far = max(curr_customer_wealth, max_wealth_so_far)
            
        return max_wealth_so_far