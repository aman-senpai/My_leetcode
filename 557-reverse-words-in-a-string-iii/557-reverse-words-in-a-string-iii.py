class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for w in range(len(s)):
            s[w] = s[w][::-1]
        return " ".join(s)