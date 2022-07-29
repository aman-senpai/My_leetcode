class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n+32) if 64 < n < 91 else c
        return ans