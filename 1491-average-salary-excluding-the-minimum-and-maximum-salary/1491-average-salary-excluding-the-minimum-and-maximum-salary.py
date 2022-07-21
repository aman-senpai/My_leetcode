class Solution:
    def average(self, salary: List[int]) -> float:
        
        Min_sal = salary[0]
        Max_sal = salary[0]
        Total_sal = 0
        
        for s in salary:
            if Min_sal > s:
                Min_sal = s
            elif Max_sal < s:
                Max_sal = s
            Total_sal += s
        return (Total_sal - (Min_sal + Max_sal)) / (len(salary) - 2)