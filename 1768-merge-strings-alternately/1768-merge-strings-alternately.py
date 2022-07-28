class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        res = ""
        w1_len = len(word1)
        w2_len = len(word2)
        while  i < w1_len or j < w2_len:
            if i < len(word1):
                res += word1[i] 
            if j <len(word2):
                res += word2[j]
            i += 1
            j += 1
        return res