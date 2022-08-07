class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = []
        
        word = ""
        for c in s:
            word += c
            if c == " ":
                word = ""
                continue
            ls.append(word)
        return len(ls[-1])