class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        
        for c in s:
            tmp = []
            if c.isalpha():
                for r in res:
                    tmp.append(r+c.lower())
                    tmp.append(r+c.upper())
            else:
                for r in res:
                    tmp.append(r+c)
            res = tmp
        return res