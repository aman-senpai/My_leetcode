class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
        res = ""
        
        i = len(num1) - 1
        j = len(num2) - 1
        
        carry = 0
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            res += str(carry % 10)
            carry = carry // 10
        return res[::-1]